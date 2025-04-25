# Context managers are great tools for resource management
# They allow to allocate and release resources precisely when we want to

# with open statements
## This ensures that the file gets closed when the with statement finishes, 
## even if there is an exception within the statement
with open("notes.txt", "w") as file:
  file.write("some to doo...")

## example of the same with full typical code
file = open("notes.txt", "w")
try:
  file.write("some to doo...")
finally:
  file.close()
  
## Another typical usage is opening and clossing database connections
## or a Lock
"""
from threading import Lock

lock = Lock()

lock.acquire()
# some code operation
lock.release()

### a better way is to use a with statement
with lock:
  # some code operation
"""

# Custom classes context managers
class ManagedFile:
  def __init__(self, filename):
    print("init")
    self.filename = filename
  
  def __enter__(self):
    print("enter")
    self.file = open(self.filename, "w")
    return self.file
  
  def __exit__(self, exc_type, exc_value, exc_traceback):
    if self.file:
      self.file.close()
    # report and handle exceptions if they occur
    if exc_type is not None:
      print("exc:", exc_type, exc_value)
      print("exception has been handled")
    print("exit")

with ManagedFile("notes.txt") as file:
  print("some stuff...")
  file.write("some to doo...")
  # triggering an exception
  ## This will stop the code with an error if activated
  # file.somemethod()
print("continuing")

# Functions implementation
from contextlib import contextmanager

@contextmanager
def open_managed_file(filename):
  f = open(filename, "w")
  try:
    yield f
  finally:
    f.close()

with open_managed_file("notes.txt") as f:
  f.write("some to doo...")
