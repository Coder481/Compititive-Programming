#https://codeforces.com/contest/296/problem/A
n=int(input())
l=[int(ele) for ele in input().split()]
d={}
for e in l:
    d[e]=d.get(e,0)+1
m=max(d.values())
if n%2==0:
    if m>n/2:print('NO')
    else:print('YES')
else:
    a=(n/2)+0.5
    if m>a:print('NO')
    else:print('YES')
