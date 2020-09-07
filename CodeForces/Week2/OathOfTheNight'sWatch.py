#https://codeforces.com/contest/768/problem/A
n,count=int(input()),0
l=[int(ele) for ele in input().split()]
l.sort()
for i in range(len(l)):
    if l[i]<l[len(l)-1] and l[i]>l[0]:
        count+=1
print(count)
