#https://codeforces.com/contest/686/problem/A
n,x=input().split()
n,x=int(n),int(x)
count=0
for _ in range(n):
    sign,ic=input().split()
    ic=int(ic)
    if sign=='+':
        x+=ic
    elif sign=='-':
        if x<ic:count+=1
        else:x-=ic
print(x,count)
