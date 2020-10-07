#https://www.codechef.com/OCT20B/problems/CHEFEZQ
for _ in range(int(input())):
    n,k=map(int,input().split())
    l=[int(ele) for ele in input().split()]
    for i in range(len(l)):
        if l[i]<k:print(i+1);break
        try:
            l[i+1]+=l[i]-k
        except:continue
    else:print((l[len(l)-1]//k)+len(l))
