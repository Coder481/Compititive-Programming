#https://codeforces.com/contest/469/problem/A
n,pl,ql=int(input()),[int(ele) for ele in input().split()],[int(el) for el in input().split()]
p,q,l,count=pl[0],ql[0],[],0
pl.pop(0),ql.pop(0)
for i in range(1,n+1):
    l.append(i)
if p+q<n:print('Oh, my keyboard!');exit()
else:
    for e in ql:
        pl.append(e)
    for f in l:
        if f in pl:
            continue
        else:print('Oh, my keyboard!');count+=1;break
    if count==0:print('I become the guy.')
