n=int(input())
l=[int(ele) for ele in input().split()]
noc=0
nop=0
for e in l:
    if e>0:
        nop+=e
    elif nop==0 or e<0:
        noc+=1
    if nop!=0 and e<0:
        nop-=1
        noc-=1
        
print(noc)
