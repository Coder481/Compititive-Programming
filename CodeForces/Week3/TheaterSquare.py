#https://codeforces.com/contest/1/problem/A
n,m,a=map(int,input().split())
if a>=max(n,m):print('1');exit()
quo1,rem1=m//a,m%a
quo2,rem2=n//a,n%a
if rem1!=0:rem1=1
if rem2!=0:rem2=1
print((quo1+rem1)*(quo2+rem2))
