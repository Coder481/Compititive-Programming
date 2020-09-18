#https://codeforces.com/contest/699/problem/A
n,s=int(input()),input()
l,nl=[int(ele) for ele in input().split()],[]
for i in range(len(s)):
    try:
        if s[i]=='R' and s[i+1]=='L':
            app=(l[i+1]-l[i])/2
            nl.append(int(app))
    except:continue
if len(nl)==0:print(-1)
else:print(min(nl))
