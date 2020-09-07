#https://codeforces.com/contest/43/problem/A
n,s,l=int(input()),set(),[]
for _ in range(n):ipt=input();l.append(ipt);s.add(ipt)
nl=[el for el in s]
arr1,arr2=[],[]
for e in l:
    if e==nl[0]:arr1.append(e)
    else:arr2.append(e)
if len(arr1)>len(arr2):print(arr1[0])
else:print(arr2[0])
