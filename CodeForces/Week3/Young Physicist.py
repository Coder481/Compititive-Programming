#https://codeforces.com/contest/69/problem/A
n,l=int(input()),[]
for _ in range(n):
    subl=[int(ele) for ele in input().split()]
    l.append(subl)
x,y,z=0,0,0
for e in l:
    x,y,z=x+e[0],y+e[1],z+e[2]
if x==0 and y==0 and z==0:
    print('YES')
else:print('NO')
