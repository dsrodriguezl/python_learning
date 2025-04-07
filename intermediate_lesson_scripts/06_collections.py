# Collections: Counter, namedtuple, OrderedDict, defaultdict, deque

# Counters are containers that store the elements as dictionary keys and their
# counts as dictionary values
from collections import Counter

a = "aaaaaabbbbbcccc"
my_counter = Counter(a)
print(my_counter)
print(my_counter.items())
print(my_counter.keys())
print(my_counter.values())

print(my_counter.most_common())
print(my_counter.most_common(1))
print(my_counter.most_common(2))
print(my_counter.most_common(1)[0])
print(my_counter.most_common(1)[0][0])

print(my_counter.elements())
print(list(my_counter.elements()))

# namedtuple are light weight objects of a custom class
from collections import namedtuple

point = namedtuple("point", "x,y")
pt = point(1, -4)
print(pt)
print(pt.x)
print(pt.y)

# OrderedDicts are like regular dictionaries but remember the order in which the
# elements were inserted
# They are less commonly used since the typical dictionaries are also capable of
# remebering this since python 3.7
from collections import OrderedDict
ordered_dict = OrderedDict()
ordered_dict["a"] = 1
ordered_dict["b"] = 2
ordered_dict["c"] = 3
ordered_dict["d"] = 4
print(ordered_dict)


ordered_dict = OrderedDict()
ordered_dict["b"] = 2
ordered_dict["c"] = 3
ordered_dict["d"] = 4
ordered_dict["a"] = 1
print(ordered_dict)

## AS mentioned before, in new python distros, regular dictionaries also 
# remember the order of insertion of elements
my_dict = {}
my_dict["a"] = 1
my_dict["b"] = 2
my_dict["c"] = 3
my_dict["d"] = 4
print(my_dict)

my_dict = {}
my_dict["b"] = 2
my_dict["c"] = 3
my_dict["d"] = 4
my_dict["a"] = 1
print(my_dict)

# defaultdicts are also similar to regular dictionaries but have a default value
# if a key was not yet inserted
from collections import defaultdict

d = defaultdict(int)
d["a"] = 1
d["b"] = 2
print(d)
print(d["a"])
print(d["b"])
print(d["c"])

d = defaultdict(float)
d["a"] = 1
d["b"] = 2
print(d)
print(d["a"])
print(d["b"])
print(d["c"])

d = defaultdict(list)
d["a"] = 1
d["b"] = 2
print(d)
print(d["a"])
print(d["b"])
print(d["c"])

d = defaultdict(str)
d["a"] = 1
d["b"] = 2
print(d)
print(d["a"])
print(d["b"])
print(d["c"])

# deques are double ended queues that can be used to add or remove elements from
# both ends efficiently
from collections import deque
d = deque()
d.append(1)
d.append(2)
print(d)
d.appendleft(3)
print(d)
d.pop()
print(d)
d.popleft()
print(d)
d.clear()
print(d)
d.extend([4,5,6])
print(d)
d.extendleft([4,5,6])
print(d)

## The order of the elements can be rotated within deques
d = deque([1, 2, 3, 4, 5, 6])
print(d)
d.rotate(1)
print(d)

d = deque([1, 2, 3, 4, 5, 6])
d.rotate(2)
print(d)

d = deque([1, 2, 3, 4, 5, 6])
d.rotate(3)
print(d)

d = deque([1, 2, 3, 4, 5, 6])
d.rotate(6)
print(d)

d = deque([1, 2, 3, 4, 5, 6])
d.rotate(-1)
print(d)

d = deque([1, 2, 3, 4, 5, 6])
d.rotate(-2)
print(d)

d = deque([1, 2, 3, 4, 5, 6])
d.rotate(-3)
print(d)
