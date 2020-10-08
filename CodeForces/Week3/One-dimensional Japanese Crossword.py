#https://codeforces.com/contest/721/problem/A
n=int(input())
s,count,l=input(),0,[]
s+='W'
for i in range(0,len(s)):
    if s[i]=='W':
        l.append(count)
        count=0
        continue
    count+=1
nl,c=[],0    
for e in l:
    if e!=0:
        c+=1
        nl.append(e)
print(c)
if c!=0:print(*nl)
