#https://codeforces.com/contest/80/problem/A
n,m=map(int,input().split())
x=n
while True:#when "True"  is used in "while" then loop will move infinity times
    n+=1
    for i in range(2,n):
        if n%i==0:        #checking next prime number
            break
    else:
      if n==m:print('YES')
      else:print('NO')
      break
