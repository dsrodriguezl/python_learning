from threading import Thread, Lock
import time

database_value = 0

def increase(lock):
  global database_value
  
  # We lock the process to prevent that another thread executes it at the same 
  # time
  # Without the aquire and release block the printed end value given by this
  # script is 1
  # Using it around the processing code the printed end value is 2
  lock.acquire()
  
  # create a local copy of the database value
  local_copy = database_value
  
  # processing
  local_copy += 1
  
  ## Delay processing in current thread for 0.1 seconds
  ### Without this sleepign time, there is no delay between threads and the 
  ### printed end value would be 2 without the aquire release lock code
  ### With the aquire release lock code, the delay does not affect the final
  ### computed value
  time.sleep(0.1)
  
  database_value = local_copy
  
  # Release the locked process, so it can be accessed by another thread
  lock.release()

if __name__ == "__main__":
  
  lock = Lock()
  print("start value", database_value)
  
  thread1 = Thread(target = increase, args = (lock,))
  thread2 = Thread(target = increase, args = (lock,))
  
  thread1.start()
  thread2.start()
  
  thread1.join()
  thread2.join()
  
  print("end value", database_value)

  print("end main")

# Alternative version of the code were instead of using an aquire release lock 
# code, the processing code is locked using a with block
# Here the release is implicit, so we do not have to remember specifying it
database_value = 0

def increase(lock):
  global database_value
  
  with lock:
    # create a local copy of the database value
    local_copy = database_value
    
    # processing
    local_copy += 1
    
    ## Delay processing in current thread for 0.1 seconds
    ### Without this sleepign time, there is no delay between threads and the 
    ### printed end value would be 2 without the aquire release lock code
    ### With the aquire release lock code, the delay does not affect the final
    ### computed value
    time.sleep(0.1)
    
    database_value = local_copy


if __name__ == "__main__":
  
  lock = Lock()
  print("start value", database_value)
  
  thread1 = Thread(target = increase, args = (lock,))
  thread2 = Thread(target = increase, args = (lock,))
  
  thread1.start()
  thread2.start()
  
  thread1.join()
  thread2.join()
  
  print("end value", database_value)

  print("end main")


# Using queues
## queues are used for thread safe and process safe data exchanges and data
## processing in multi threaded or multi processing environments
## They are linear data structures data follow the Firs In First Out (FIFO)
## principle
from queue import Queue
from threading import Thread, Lock, current_thread

def worker(q, lock):
  while True:
    value = q.get()
    
    # processing
    with lock:
      print(f"in {current_thread().name} got {value}")
    
    # Needed when we finish processing within a queue 
    q.task_done()

if __name__ == "__main__":
  
  q = Queue()
  lock = Lock()
  num_threads = 10
  
  for i in range(num_threads):
    thread = Thread(target = worker, args = (q, lock))
    # we use daemon threads, which are background threads that terminate when 
    # the main thread terminates
    # Here this effectively terminates the processing of the infinite while loop
    # Without this daemon loop we would need to use a break statement at the end
    # of the worker function, to indicate the termination condition and
    # ensure that the loop stops
    thread.daemon = True
    thread.start()
  
  for i in range(1, 21):
    q.put(i)

  q.join()
  
  print("end main")
