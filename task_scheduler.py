import abc

class TaskScheduler(object):
    __meta__ = abc.ABCMeta

    def __init__(self, task_queue, processors):
        super(TaskScheduler, self).__init__()
        self.__task_queue = task_queue
        self.__processors = processors

    @property
    def task_queue(self): return self.__task_queue

    @property
    def processors(self): return self.__processors

    @abc.abstractmethod
    def schedule_next_task(self):
        raise Exception("NotImplemented")

class FifoTaskScheduler(TaskScheduler):
    """docstring for FifoTaskScheduler"""
    def __init__(self, task_queue, processors):
        super(FifoTaskScheduler, self).__init__(task_queue, processors)
    
    def schedule_next_task(self):
        for p in self.processors:
            if p.task:
                return
        
        _task = self.task_queue.front()
        for p in self.processors:
            try:
                p.task = _task
                return
            except:
                pass
        else:
            self.task_queue.append(_task)
        