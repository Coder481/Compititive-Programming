#https://codeforces.com/contest/520/problem/A
n,s=int(input()),input()
alpha='abcdefghijklmnopqrstuvwxyz'
s,count=s.lower(),0
for e in alpha:
    if e not in s:
        count+=1
        break
if count==0:print('YES')
else:print('NO')
