# Python Functions Reference

## Date & Datetime

```python
from datetime import datetime, date, timedelta
```

### Creating Dates

```python
d1 = date(2026, 4, 6)
d2 = date.today()
dt = datetime.now()
dt = datetime.strptime("2026-04-06", "%Y-%m-%d")  # parse from string
```

### Comparison Operators

All standard operators work directly on `date` and `datetime` objects:

```python
d1 == d2   # equal
d1 != d2   # not equal
d1 < d2    # before
d1 > d2    # after
d1 <= d2
d1 >= d2
```

### Difference Between Dates

```python
diff = d2 - d1           # returns timedelta
diff.days                # number of days
diff.total_seconds()     # total seconds
```

### Adding / Subtracting Days

```python
d1 + timedelta(days=7)   # 7 days later
d1 - timedelta(days=3)   # 3 days before
```

### Useful Attributes

```python
d1.year          # 2026
d1.month         # 4
d1.day           # 6
dt.weekday()     # 0=Monday ... 6=Sunday
dt.isoweekday()  # 1=Monday ... 7=Sunday
```

### Format Date to String

```python
d1.strftime("%Y-%m-%d")   # "2026-04-06"
d1.strftime("%d/%m/%Y")   # "06/04/2026"
d1.isoformat()            # "2026-04-06"
```

### Common Interview Patterns

```python
# check if date is weekend
d1.weekday() >= 5

# days between two dates
abs((d2 - d1).days)

# sort a list of date strings (ISO format sorts lexicographically = chronologically)
dates = ["2026-01-10", "2025-12-01", "2026-04-06"]
dates.sort()
```

---

## String Methods

```python
s = "hello world"

s.split()            # ['hello', 'world']
s.split(',')         # split by delimiter
' '.join(['a','b'])  # 'a b'
s.strip()            # remove leading/trailing whitespace
s.replace('l','L')   # 'heLLo worLd'
s.find('o')          # 4 (first index, -1 if not found)
s.count('l')         # 3
s.startswith('he')   # True
s.endswith('ld')     # True
s.lower()            # 'hello world'
s.upper()            # 'HELLO WORLD'
s.isdigit()          # False
s.isalpha()          # False
s.isalnum()          # False
ord('a')             # 97
chr(97)              # 'a'
s[::-1]              # reverse string
```

---

## List / Array

```python
a = [3, 1, 4, 1, 5]

a.append(6)           # add to end
a.pop()               # remove from end
a.pop(0)              # remove at index
a.insert(1, 99)       # insert 99 at index 1
a.remove(4)           # remove first occurrence of value
a.index(5)            # index of value
a.count(1)            # count occurrences
a.reverse()           # in-place reverse
a[::-1]               # reversed copy
min(a), max(a)        # min and max
sum(a)                # sum
len(a)                # length
sorted(a)             # sorted copy (original unchanged)
a.sort()              # in-place sort
a.sort(reverse=True)  # descending
```

---

## Sorting with Key

```python
words = ["banana", "apple", "cherry"]
words.sort(key=len)                    # sort by length
words.sort(key=lambda x: x[-1])       # sort by last character

pairs = [(1, 3), (2, 1), (0, 2)]
pairs.sort(key=lambda x: x[1])        # sort by second element
pairs.sort(key=lambda x: (x[1], x[0]))# sort by second, then first
```

---

## Dictionary

```python
d = {}
d['a'] = 1
d.get('b', 0)           # return 0 if key missing (safe access)
d.keys()                # dict_keys
d.values()              # dict_values
d.items()               # dict_items — use in for loops
d.setdefault('c', [])   # set default if key missing
'a' in d                # True
del d['a']
```

---

## Collections

```python
from collections import Counter, defaultdict, deque

# Counter
c = Counter([1, 2, 2, 3])   # {2:2, 1:1, 3:1}
c.most_common(2)             # [(2,2), (1,1)]
c['x']                       # 0 (no KeyError)

# defaultdict
dd = defaultdict(int)         # default 0
dd = defaultdict(list)        # default []

# deque (double-ended queue — O(1) append/pop on both ends)
dq = deque()
dq.append(1)         # right
dq.appendleft(0)     # left
dq.pop()             # right
dq.popleft()         # left
deque([1,2,3], maxlen=3)  # fixed-size sliding window
```

---

## Heap (Priority Queue)

```python
import heapq

h = []
heapq.heappush(h, 3)
heapq.heappush(h, 1)
heapq.heappop(h)          # 1 (min-heap by default)

heapq.heapify(lst)        # convert list to heap in-place O(n)
heapq.nlargest(k, lst)    # k largest elements
heapq.nsmallest(k, lst)   # k smallest elements

# Max-heap trick: negate values
heapq.heappush(h, -val)
val = -heapq.heappop(h)
```

---

## Set

```python
s = {1, 2, 3}
s.add(4)
s.remove(2)          # raises KeyError if missing
s.discard(2)         # safe remove
2 in s               # O(1) lookup

s1 | s2              # union
s1 & s2              # intersection
s1 - s2              # difference
s1 ^ s2              # symmetric difference
```

---

## Binary Search (bisect)

```python
import bisect

a = [1, 3, 5, 7, 9]
bisect.bisect_left(a, 5)   # 2 — leftmost index to insert 5
bisect.bisect_right(a, 5)  # 3 — rightmost index to insert 5
bisect.insort(a, 6)        # insert in sorted order
```

---

## Math

```python
import math

math.inf              # infinity
-math.inf             # negative infinity
math.floor(3.7)       # 3
math.ceil(3.2)        # 4
math.sqrt(16)         # 4.0
math.log(8, 2)        # 3.0
abs(-5)               # 5
pow(2, 10)            # 1024
divmod(10, 3)         # (3, 1) — quotient and remainder
```

---

## Useful Built-ins

```python
enumerate([10,20,30])         # (0,10),(1,20),(2,30)
zip([1,2], [3,4])             # (1,3),(2,4)
zip(*matrix)                  # transpose 2D list
map(int, ['1','2','3'])       # [1,2,3]
filter(lambda x: x>2, lst)   # keep elements where condition is True
any([False, True, False])     # True
all([True, True, False])      # False
```

---

## itertools

```python
from itertools import combinations, permutations, product, accumulate

combinations([1,2,3], 2)       # (1,2),(1,3),(2,3)
permutations([1,2,3], 2)       # all ordered pairs
product([1,2], [3,4])          # cartesian product
accumulate([1,2,3,4])          # [1,3,6,10] (prefix sums)
```

---

## Type Conversions

```python
int("42")             # 42
int("1010", 2)        # 10 (binary to int)
str(42)               # "42"
bin(10)               # '0b1010'
hex(255)              # '0xff'
list("abc")           # ['a','b','c']
list(range(5))        # [0,1,2,3,4]
set([1,1,2])          # {1,2}
tuple([1,2,3])        # (1,2,3)
dict(zip(keys, vals)) # build dict from two lists
```
