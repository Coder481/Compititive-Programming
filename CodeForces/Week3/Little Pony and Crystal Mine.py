#https://codeforces.com/contest/454/problem/A
n=int(input())
for i in range(1,((n+1)//2)+1):
    for j in range(1,n+1):
        c=(n+1)//2
        if  j>=c-(i-1) and j<=c+(i-1):
            print('D',end='')
        else:print('*',end='')
    print()
for i in range(((n+1)//2)+1,n+1):
    for j in range(1,n+1):
        c=(n+1)//2
        if j>=c-(n-i) and j<=c+(n-i):print('D',end='')
        else:print('*',end='')
    print()
