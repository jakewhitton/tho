import time
from threading import Thread
import random

# Problem: create three threads as part of an application:
#   1. Spawns threads 2 & 3, spins in an empty loop for 10 seconds and then signals them to shutdown
#   2. Generates a random number every second and puts it into a global list
#   3. Pops number from the global list, adds one to the number, and prints it
#
# Hint: use threading.Thread class, see documentation here:
# https://docs.python.org/3/library/threading.html#threading.Thread

numbers = []
shutdown = False

def thread_1(): # main thread in python

    global shutdown
    global numbers
    
    t2 = Thread(target=thread_2)
    t3 = Thread(target=thread_3)

    t2.start()
    t3.start()

    time.sleep(10) # wait for 10 seconds in the main thread
    shutdown=True

    # Once you give the signal for both threads to close, call join() on them
    #
    # join() waits for the thread's function to return on its own and then
    # cleans up the thread object afterwards
    #
    # Warning: join() will spin indefinitely if you do not send some message to
    # the thread that it needs to return -- use global variables or a state
    # object that you pass in with the args kwargsas i of the Thread() constructor
    t2.join()
    t3.join()

def thread_2():
    while True:
    
        num = random.randint(0, 1e5)
        numbers.append(num)
        time.sleep(1)

        if shutdown:
            return

def thread_3():
    i = 0
    while True:
        if numbers:
            i += 1
            num = numbers.pop()
            print(f'Number {i} is {num+1}')

        if shutdown:
            return
        
thread_1()