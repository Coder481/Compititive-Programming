#https://codeforces.com/contest/271/problem/A
n=int(input())
while True:
    n+=1
    if len(set(str(n)))==len(str(n)):print(n);break
