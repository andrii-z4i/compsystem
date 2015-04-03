from task import Task
from random import randint, sample

class TaskGenerator(object):
    """docstring for TaskGenerator"""
    def __init__(self, min_complexity, max_complexity, processors):
        super(TaskGenerator, self).__init__()
        self.__min_complexity = min_complexity
        self.__max_complexity = max_complexity
        self.__processors = processors
        self.__task_counter = 0

    def _generate_list_of_possible_processors(self):
        _processors_number = randint(1, len(self.__processors))
        _processors = sample([p.id for p in self.__processors], _processors_number)
        return _processors

    def new_task(self):
        self.__task_counter += 1
        _processor_ids = self._generate_list_of_possible_processors()
        _processors_performance = [p.performance for p in self.__processors if p.id in _processor_ids]
        _min_performance = min(_processors_performance)
        _complexity = randint(_min_performance * self.__min_complexity, _min_performance * self.__max_complexity)
        _task = Task(self.__task_counter, _complexity, _processor_ids)
        return _task
        
