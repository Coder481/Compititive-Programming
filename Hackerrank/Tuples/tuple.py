#https://www.hackerrank.com/challenges/python-tuples/problem
n=int(input())
l=input().split()
l1=[]

for e in l:
     x=int(e)
     l1.append(x)
t=tuple(l1)

print(hash(t))
