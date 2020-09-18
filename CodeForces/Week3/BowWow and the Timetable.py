#https://codeforces.com/contest/1204/problem/A
bi=input()
n=int(bi,2)
i,count=0,0
while True:
    if 4**i<n:count+=1
    elif 4**i>=n:break
    i+=1
print(count)
