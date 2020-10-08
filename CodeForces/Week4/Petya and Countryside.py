#https://codeforces.com/contest/66/problem/B
n=int(input())
l=[int(ele) for ele in input().split()]
ans=[]
for i in range(len(l)):
    count=1
    if i!=0:
        for j in range(i,0,-1):
            if l[j]>=l[j-1]:count+=1;continue
            else:break
    if i!=(len(l)-1):
        for j in range(i+1,n):
            if l[j]<=l[j-1]:count+=1;continue
            else:break
    ans.append(count)
    
print(max(ans))
