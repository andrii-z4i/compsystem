from threading import Thread
from time import sleep
from task import Task

class Processor(Thread):
    """docstring for Processor"""
    def __init__(self, id, additional_work = None, *args, **kwargs):
        super(Processor, self).__init__(*args, **kwargs)
        self.__performance = 1
        self.__current_task = None
        self.__force_stop = False
        self.__id = id
        self.__processed_tasks_number = 0
        self.__additional_work = additional_work
        self.__performed_operations = 0
        self.__remaining_work = 0

    @property
    def id(self): return self.__id

    @property
    def processed_tasks_number(self): return self.__processed_tasks_number

    @processed_tasks_number.setter
    def processed_tasks_number(self, value): self.__processed_tasks_number = value

    @property
    def performance(self): return self.__performance

    @performance.setter
    def performance(self, value): self.__performance = value

    @property
    def task(self): return self.__current_task

    @task.setter
    def task(self, value):
        if not value or not isinstance(value, Task):
            self.__current_task = None
            return 

        if self.id not in value.processor_ids:
            raise Exception("Task can't be assigned for this processor")
        else:
            self.__current_task = value
            self.remaining_work = value.complexity

    @property
    def performed_operations(self): return self.__performed_operations

    @performed_operations.setter
    def performed_operations(self, value): self.__performed_operations = value

    @property
    def remaining_work(self): return self.__remaining_work

    @remaining_work.setter
    def remaining_work(self, value): self.__remaining_work = value

    def force_stop(self):
        self.__force_stop = True

    def run(self):
        while not self.__force_stop:
            if self.__additional_work:
                self.__additional_work(self)
            
