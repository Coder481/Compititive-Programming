#https://codeforces.com/contest/143/problem/A
r1,r2=map(int,input().split())
c1,c2=map(int,input().split())
d1,d2=map(int,input().split())
l1,l2,count=[],[],0
for i in range(1,10):
    for j in range(1,10):
        if i+j==r1 and i!=j:l1.append([i,j])
        if i+j==r2 and i!=j:l2.append([i,j])
for k in range(len(l1)):
    for l in range(len(l2)):
        if l1[k][1]!=l2[l][0] and l1[k][1]+l2[l][0]==c1 and l1[k][0]!=l2[l][1] and l1[k][0]+l2[l][1]==c2:
            if l1[k][0]!=l2[l][0] and l1[k][0]+l2[l][0]==d2 and l1[k][1]!=l2[l][1] and l1[k][1]+l2[l][1]==d1:
                print(l1[k][1],l1[k][0])
                print(*l2[l])
                count+=1
                break
    if count!=0:break
if count==0:print(-1)
