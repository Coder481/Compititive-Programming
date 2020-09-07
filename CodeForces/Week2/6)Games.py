n=int(input())
nog=n*(n-1)
L=[]
count=0
for _ in range(n):
    l=[int(ele) for ele in input().split()]
    L.append(l)
for e in L:
    for i in range(0,len(L)):
        if e==L[i]:
            continue
        if e[0]==L[i][1]:
            count+=1
print(count)
