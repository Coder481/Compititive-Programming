#https://codeforces.com/contest/255/problem/A
n,chest,biceps,back,count=int(input()),0,0,0,0
l=[int(ele) for ele in input().split()]
for e in l:
    if count%3==0:
        chest,count=chest+e,count+1
    elif (count-1)%3==0:
        biceps,count=biceps+e,count+1
    elif (count-2)%3==0:
        back,count=back+e,count+1
if chest==max(chest,biceps,back):print('chest')
elif biceps==max(chest,biceps,back):print('biceps')
elif back==max(chest,biceps,back):print('back')
