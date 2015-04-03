class Task(object):
    """docstring for Task"""
    def __init__(self, id, complexity, processor_ids):
        super(Task, self).__init__()
        self.__id = id
        self.__complexity = complexity
        self.__processor_ids = processor_ids

    def __repr__(self):
        return "Task: id(%d), complexity(%d), processor ids(%s)" % (self.__id, self.__complexity, self.__processor_ids)

    @property
    def complexity(self): return self.__complexity

    @complexity.setter
    def complexity(self, value): self.__complexity = value
    
    @property
    def processor_ids(self): return self.__processor_ids

    @property
    def id(self): return self.__id
