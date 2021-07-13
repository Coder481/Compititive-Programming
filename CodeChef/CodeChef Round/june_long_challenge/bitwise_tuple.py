
for i in range(int(input())):
     n, m = map(int,input().split())
     a = pow(2,n,1000000007)-1
     print(pow(a,m,1000000007))