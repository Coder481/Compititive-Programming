n=int(input())
l=[int(ele) for ele in input().split()]
sereja=0
dima=0
for i in range(1,n+1):
    if i%2!=0:
        sereja+=max(l[0],l[len(l)-1])
        l.remove(max(l[0],l[len(l)-1]))
    elif i%2==0:
        dima+=max(l[0],l[len(l)-1])
        l.remove(max(l[0],l[len(l)-1]))
print(sereja,dima)
