#https://codeforces.com/contest/282/problem/A
n,x=int(input()),0
for _ in range(n):
    s=input()
    if '+' in s:x+=1
    elif '-' in s:x-=1
print(x)
