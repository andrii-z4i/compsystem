from threading import Lock

class TaskQueue(object):
    def __init__(self):
        super(TaskQueue, self).__init__()
        self.__queue = list()
        self.__lock = Lock()

    @property
    def tasks(self): return self.__queue

    def append(self, value):
        self.__lock.acquire()
        self.__queue.append(value)
        self.__lock.release()

    def front(self):
        return self.pop(0)

    def pop(self, index):
        self.__lock.acquire()
        if not len(self.__queue):
            self.__lock.release()
            return None
            
        value = self.__queue.pop(index)
        self.__lock.release()
        return value