#https://codeforces.com/contest/467/problem/A
n,count=int(input()),0
for _ in range(n):
    p,q=map(int,input().split())
    if q-p>1:count+=1
print(count)
