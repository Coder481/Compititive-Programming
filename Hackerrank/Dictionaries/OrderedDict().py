#https://www.hackerrank.com/challenges/py-collections-ordereddict/problem
N=int(input())
d={}
lot=[]
for i in range(N):
    x=input()
    l=[]
    for e in x.split():
        l.append(e)
    p=int(l.pop())
    s=''
    for j in l:
        s+=j
        if j==l[len(l)-1]:
            break
        s+=' '
    lot.append((s,p))
    d[s]=p

for k,v in d.items():
    total=0
    for e in lot:
        if e[0]==k:
            total+=e[1]
    print(k,total)
