from multiprocessing import Process, Value, Array, Lock
import time

# Share values across processes
def add_100(number, lock):
  for i in range(100):
    time.sleep(0.01)
    with lock:
      number.value += 1

if __name__ == "__main__":
  lock = Lock()
  shared_number = Value('i', 0)
  print("Number at beginning is", shared_number.value)
  
  p1 = Process(target = add_100, args = (shared_number, lock))
  p2 = Process(target = add_100, args = (shared_number, lock))
  
  p1.start()
  p2.start()
  
  p1.join()
  p2.join()
  
  print("Number at end is", shared_number.value)

# Share arrays across processes
def add_100(numbers, lock):
  for i in range(100):
    time.sleep(0.01)
    for i in range(len(numbers)):
      with lock:
        numbers[i] +=1

if __name__ == "__main__":
  lock = Lock()
  shared_array = Array('d', [0.0, 100.0, 200.0])
  print("Array at beginning is", shared_array[:])
  
  p1 = Process(target = add_100, args = (shared_array, lock))
  p2 = Process(target = add_100, args = (shared_array, lock))
  
  p1.start()
  p2.start()
  
  p1.join()
  p2.join()
  
  print("Array at end is", shared_array[:])

# Using queues to exchange elements between processes
from multiprocessing import Queue
def square(numbers, q):
  for i in numbers:
    queue.put(i * i)

def make_negative(numbers, q):
  for i in numbers:
    queue.put(-1 * i)

if __name__ == "__main__":
  
  numbers = range(1, 6)
  q = Queue()
  
  p1 = Process(target = square, args = (numbers, q))
  p2 = Process(target = make_negative, args = (numbers, q))
  
  p1.start()
  p2.start()
  
  p1.join()
  p2.join()
  
  # I cannot understand why this is not printing anything
  while not q.empty():
    print(q.get())

# Process pool
# Use to manage multiple processes
# They control pools of worker processes to which jobs can be submitted
# Manage available processe for you and split data into smaller chunks that
# can be processed in parallel by the multiple processes
from multiprocessing import Pool

def cube(number):
  return number * number * number

if __name__ == "__main__":
  
  numbers = range(10)
  pool = Pool()
  
  # Pool has several methods, the most important are map, apply, join, and close
  result = pool.map(cube, numbers)
  # pool.apply(cube, numbers[3]) # This will execute a single process
  
  pool.close()
  pool.join()
  
  print(result)
  













