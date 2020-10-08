#https://codeforces.com/contest/950/problem/A
l,r,a=map(int,input().split())
if l==r:
    if a%2==0:print(l+r+a)
    else:print(l+r+a-1)
    exit()
m,M=min(l,r),max(l,r)
ans,M=2*m,M-m
if M==a:print(ans+M+a);exit()
elif a<M:print(ans+a+a);exit()
elif a>M:
    ans,a=ans+M*2,a-M
    if a%2==0:print(ans+a)
    else:print(ans+a-1)
