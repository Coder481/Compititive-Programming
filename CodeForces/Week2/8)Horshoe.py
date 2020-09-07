#https://codeforces.com/contest/228/problem/A
l=[int(ele) for ele in input().split()]
d={}
for e in l:
    d[e]='.'
lod=len(d)
print(4-lod)
