#https://codeforces.com/contest/365/problem/A
n, k = map(int, input().split())
k_good = {str(i) for i in range(k+1)}
count = 0

for i in range(n):
    unique = set(input())
    if k_good <= unique:
        count += 1

print(count)
