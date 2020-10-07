#https://codeforces.com/contest/158/problem/A
n,k=map(int,input().split())
l=[int(ele) for ele in input().split()]
mscr=l[k-1]
l.reverse()
ans=len(l)-l.index(mscr)
if mscr==0:
    for e in l:
        if e==0:ans-=1
print(ans)
