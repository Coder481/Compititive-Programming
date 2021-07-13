
for _ in range(int(input())):
    n,x,k = map(int,input().split())
    # forward
    if(x%k==0):print('YES')
    # backward
    elif((n+1-x)%k == 0):print('YES')
    # else otherwise
    else:print('NO')