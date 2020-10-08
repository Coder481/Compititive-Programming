#https://codeforces.com/contest/456/problem/A
n,positive,negative,count=int(input()),0,0,0
for _ in range(n):
    a,b=map(int,input().split())
    if positive<1:
        if a-b>0:positive+=1;count+=1
    if negative<1:
        if a-b<0:negative+=1;count+=1
if count==2:print('Happy Alex')
else:print('Poor Alex')
