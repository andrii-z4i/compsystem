import abc
import copy

class TaskScheduler(object):
    __meta__ = abc.ABCMeta

    def __init__(self, task_queue, processors):
        super(TaskScheduler, self).__init__()
        self.__task_queue = task_queue
        self.__processors = processors
        self.__ids = dict([(p.id, p) for p in processors])

    @property
    def task_queue(self): return self.__task_queue

    @property
    def processors(self): return self.__processors

    @property
    def processors_map(self): return self.__ids

    @abc.abstractmethod
    def schedule_next_task(self):
        raise Exception("NotImplemented")

class FifoTaskScheduler(TaskScheduler):
    """docstring for FifoTaskScheduler"""
    def __init__(self, task_queue, processors):
        super(FifoTaskScheduler, self).__init__(task_queue, processors)
    
    def schedule_next_task(self):
        if not len(self.task_queue.tasks):
            return

        _top_task = self.task_queue.tasks[0]

        for processor_id in _top_task.processor_ids:
            if self.processors_map[processor_id].task:
                return

        _task = self.task_queue.front()
        for processor_id in _task.processor_ids:
        #for p in self.processors:
            try:
                self.processors_map[processor_id].task = copy.copy(_task)
            except Exception, e:
                self.task_queue.append(_task)
                print e
                return
        