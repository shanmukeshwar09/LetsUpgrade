from collections import deque

q = deque()
q.append(10)
q.append(100)
q.append(1000)
q.append(10000)

print("Initial Queue is:",q)
print(q.popleft())
print(q.popleft())
print("After Removing elements:",q)
