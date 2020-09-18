#https://codeforces.com/contest/667/problem/A
from math import pi
d, h, v, e = [int(x) for x in input().split(" ")]
t = h/((4.0*v)/(pi*d**2)-e)
if t < 0:
    print("NO")
    exit()
print("YES")
print(t)
