#https://codeforces.com/contest/785/problem/A
n,count=int(input()),0
for _ in range(n):
    s=input()
    if s[0]=='T':count+=4
    elif s[0]=='C':count+=6
    elif s[0]=='O':count+=8
    elif s[0]=='D':count+=12
    elif s[0]=='I':count+=20
print(count)
