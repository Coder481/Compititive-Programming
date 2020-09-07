#https://codeforces.com/contest/136/problem/A
n=int(input())
l=[int(ele) for ele in input().split()]
ol=[]
for i in range(1,n+1):
    ol.append(l.index(i)+1)
print(*ol)
