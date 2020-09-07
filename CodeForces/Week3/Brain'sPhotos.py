#https://codeforces.com/contest/707/problem/A
row,col=map(int,input().split())
l=[]
for _ in range(row):
    ipt=input().split()
    for e in ipt:l.append(e)
for p in l:
    if p=='C' or p=='Y' or p=='M':print('#Color');break
else:print('#Black&White')
