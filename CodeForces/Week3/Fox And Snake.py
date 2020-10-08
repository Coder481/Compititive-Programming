#https://codeforces.com/contest/510/problem/A
n,m=map(int,input().split())
l=[]
for i in range(1,n+1):
    s=''
    for j in range(1,m+1):
        if i%2!=0:s+='#'
        elif i%2==0 and i%4!=0:
            if j==m:s+='#'
            else:s+='.'
        elif i%4==0:
            if j==1:s+='#'
            else:s+='.'
    l.append(s)
for e in l:print(e)
