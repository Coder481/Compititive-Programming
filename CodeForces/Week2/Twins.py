#https://codeforces.com/contest/160/problem/A
n,l,sum=int(input()),[int(ele) for ele in input().split()],0
for e in l:sum+=e
l.sort(),l.reverse()
osum,count=0,0
for e in l:
    osum+=e
    count+=1
    if osum>sum-osum:
        break
print(count)
