# Process: Instance of a program (e.g. A browser window, or a python interpreter)
# Thread: Is an entity within a process that can be scheduled for execution,
# also known as lighweight processes
# A process can have multiple threads within it
# Processes take advantage of CPUs and cores, and have separate memory spaces
# are interruptable/killable, heavyweigth (take space in memory)
# starting them is slower than starting a thread
# inter-process communication is complicated
# Threads within a process share memory space
# Threads are lightweight, faster to start than a process, great for I/O-bound 
# tasks (input/output), not interruptable/killable
# Only one thread can be used at a time (no parallel computation with 
# multithreading)
# Global Interpreter Lock (GIL): It is a lock that allows only one thread at a 
# time to execute in Python
# It is needed in CPython because memory management is not thread-safe

# multiprocessing
from multiprocessing import Process
import os
import time

processes = []
num_processes = os.cpu_count()

def square_numbers():
  for i in range(100):
    i * i
    time.sleep(0.1)

# Create processes
for i in range(num_processes):
  # If the target function has arguments they can be passed in a tuple to the
  # argument "args" of the Process function
  p = Process(target = square_numbers)
  processes.append(p)

# start processes
for p in processes:
  p.start()

# join processes
## We wait for a process to finish and until all have finished we block the 
## main thread
for p in processes:
  p.join()

print("end main")

# multithreading
from threading import Thread
import os
import time

threads = []
num_threads = 10

def square_numbers():
  for i in range(100):
    i * i
    time.sleep(0.1)

# Create processes
for i in range(num_threads):
  # If the target function has arguments they can be passed in a tuple to the
  # argument "args" of the Thread function
  t = Thread(target = square_numbers)
  threads.append(t)

# start processes
for t in threads:
  t.start()

# join processes
## We wait for a process to finish and until all have finished we block the 
## main thread
for t in threads:
  t.join()

print("end main")
