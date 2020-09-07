#https://codeforces.com/contest/208/problem/A
s,l=input(),[]
for e in s.split('WUB'):
    if len(e)!=0:l.append(e)
print(*l)
