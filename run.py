from processor import Processor
from time import sleep
from task_generator import TaskGenerator
from task_queue import TaskQueue
from random import randint
import thread
from task_scheduler import FifoTaskScheduler

PROCESSORS_NUMBER = 10
PROCESSORS = []
MIN_PERFORMANCE = 5  # ms
MAX_PERFORMANCE = 200 # ms
TEST_TIME = 10
FINISH = False

task_queue = TaskQueue()

def generate_tasks(interval, task_queue):
    global FINISH, PROCESSORS, MIN_PERFORMANCE, MAX_PERFORMANCE
    _taskGenerator = TaskGenerator(MIN_PERFORMANCE, MAX_PERFORMANCE, PROCESSORS)
    while not FINISH:
        sleep(interval)
        if randint(0, 1):
            task_queue.append(_taskGenerator.new_task())

def schedule_tasks(interval, scheduler):
    global FINISH
    while not FINISH:
        sleep(interval)
        scheduler.schedule_next_task()


for i in xrange(PROCESSORS_NUMBER):
    _processor = Processor(i)
    _processor.performance = randint(MIN_PERFORMANCE, MAX_PERFORMANCE)
    _processor.start()
    PROCESSORS.append(_processor)

scheduler = FifoTaskScheduler(task_queue, PROCESSORS)

thread.start_new_thread(generate_tasks, (0.001, task_queue))
thread.start_new_thread(schedule_tasks, (0.001, scheduler))

sleep(TEST_TIME)

FINISH = True
print len(task_queue.tasks)

processed_tasks_number = 0
for processor in PROCESSORS:
    processor.force_stop()
    processed_tasks_number += processor.processed_tasks_number

print processed_tasks_number
sleep(0.001)