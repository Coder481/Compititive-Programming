#https://codeforces.com/contest/294/problem/A
n=int(input())
l=[int(ele) for ele in input().split()]
m=int(input())
for _ in range(m):
    ls=[int(el) for el in input().split()]
    x,y=ls[0]-1,ls[1]
    if x==0:
        l[0]=l[0]-y
        if n!=1:
            l[1]+=l[0]
        l[0]=0
    elif x==n-1:
        l[n-1]=y-1
        l[n-2]+=l[n-1]
        l[n-1]=0
    else:
        l[x-1]+=y-1
        l[x+1]+=l[x]-y
        l[x]=0
for e in l:
    print(e)
