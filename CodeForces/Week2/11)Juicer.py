#https://codeforces.com/contest/709/problem/A
n,b,d=[int(ele) for ele in input().split()]
l=[int(el) for el in input().split()]
count,sum=0,0
for e in l:
    if e>b:continue
    sum+=e
    if sum>d:
        sum=0
        count+=1
print(count)
