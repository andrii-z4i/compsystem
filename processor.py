from threading import Thread
from time import sleep
from task import Task

class Processor(Thread):
    """docstring for Processor"""
    def __init__(self, id, *args, **kwargs):
        super(Processor, self).__init__(*args, **kwargs)
        self.__performance = 1
        self.__current_task = None
        self.__force_stop = False
        self.__id = id
        self.__processed_tasks_number = 0

    @property
    def id(self): return self.__id

    @property
    def processed_tasks_number(self): return self.__processed_tasks_number

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
            #print "processor(%d), task(%s)" % (self.__id, self.__current_task)

    def force_stop(self):
        self.__force_stop = True

    def run(self):
        while not self.__force_stop:
            sleep(0.001)
            if not self.task:
                continue

            self.task.complexity -= self.performance
            if self.task.complexity < 0:
                self.__processed_tasks_number += 1
                self.task = None
            
