#https://codeforces.com/contest/9/problem/A
l=[int(ele) for ele in input().split()]
m=max(l)
a,b=7-m,6
k=int(6/a)
if a==4:print('2/3')
if 6%a==0:print('1/%d'%k)
elif a==5:print('5/6')
