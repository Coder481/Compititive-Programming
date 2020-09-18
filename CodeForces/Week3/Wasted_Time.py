#https://codeforces.com/contest/127/problem/A
import math
n,k=map(int,input().split())
x1,y1=map(int,input().split())
time=0
for _ in range(n-1):
    x2,y2=map(int,input().split())
    dis=math.sqrt((x2-x1)**2+(y2-y1)**2)
    t=dis/50
    time+=t
    x1,y1=x2,y2
time*=k
print('%.9f'%time)
