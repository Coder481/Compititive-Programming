#https://www.hackerrank.com/challenges/py-collections-deque/problem
from collections import deque
d=deque()
for _ in range(int(input())):
    w=input().split()
    word=w[0]
    if len(w)>1:
        digit=int(w[len(w)-1])
        if word=='append':
            d.append(digit)
        elif word=='appendleft':
            d.appendleft(digit)
    else:
        if word=='pop':
            d.pop()
        elif word=='popleft':
            d.popleft()
print(*d)
