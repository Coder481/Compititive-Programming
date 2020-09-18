#https://codeforces.com/contest/382/problem/A
l=[ele for ele in input().split('|')]
s=input()
for i in range(0,len(s)):
    left,right=len(l[0]),len(l[1])
    if left>right:l[1]+=s[i]
    elif right>left:l[0]+=s[i]
    else:l[0]+=s[i]
if len(l[0])!=len(l[1]):print('Impossible')
else:
    opt=''
    l.insert(1,'|')
    for e in l:
        opt+=e
    print(opt)
