#https://codeforces.com/contest/483/problem/A
l, r = [int(i) for i in input().split()]
if r - l < 2: print(-1)
elif l % 2 == 0: print(l, l + 1, l + 2)
elif r - l > 2: print(l + 1, l + 2, l + 3)
else: print(-1)
