#https://codeforces.com/contest/270/problem/A
n,l=int(input()),[]
for _ in range(n):
    e=int(input())
    ans=360/(180-e)
    if ans==int(ans):l.append('YES')
    else:l.append('NO')
for e in l:print(e)
