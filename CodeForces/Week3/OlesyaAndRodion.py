#https://codeforces.com/contest/584/problem/A
n,t=map(int,input().split())
for i in range(10**(n-1),10**n):
    if i%t==0:print(i);break
else:print('-1')
