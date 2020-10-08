#https://codeforces.com/contest/681/problem/A
n=int(input())
l,count=[],0
for _ in range(n):
    l=[ele for ele in input().split()]
    if int(l[1])>=2400:
        if (int(l[2])-int(l[1]))>0:
            count+=1
if count!=0:print('YES')
else:print("NO")
