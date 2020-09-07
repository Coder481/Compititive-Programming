#https://codeforces.com/contest/71/problem/A
n=int(input())
l=[]
for _ in range(n):
    s=input()
    if len(s)<=10:
        l.append(s)
        continue
    else:
        st=''
        sl=[s[0],len(s)-2,s[len(s)-1]]
        for e in sl:
            st+=str(e)
        l.append(st)
for e in l:
    print(e)
