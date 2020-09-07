#https://codeforces.com/contest/677/submission/90468872

try:
    n,h=input().split()
    n=int(n)
    h=int(h)
    l=[int(ele) for ele in input().split()]
    width=0
    for e in l:
        if e>h:
            width+=2
        else:
            width+=1
    print(width)
except Exception:
    pass
