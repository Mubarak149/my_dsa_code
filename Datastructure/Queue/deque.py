# Import the deque class
from collections import deque

# Create a deque with some elements
dq = deque([1, 2, 3, 4])

# Append an element to the right end
dq.append(5)
print(dq) # deque([1, 2, 3, 4, 5])

# Append an element to the left end
dq.appendleft(0)
print(dq) # deque([0, 1, 2, 3, 4, 5])

# Pop an element from the right end
dq.pop()
print(dq) # deque([0, 1, 2, 3, 4])

# Pop an element from the left end
dq.popleft()
print(dq) # deque([1, 2, 3, 4])

# Access an element by index
print(dq[2]) # 3

# Insert an element at a given index
dq.insert(2, 10)
print(dq) # deque([1, 2, 10, 3, 4])

# Remove an element by value
dq.remove(10)
print(dq) # deque([1, 2, 3, 4])

# Count the number of occurrences of an element
print(dq.count(2)) # 1
