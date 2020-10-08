#https://codeforces.com/contest/61/problem/A
s1,s2,s=input(),input(),''
for i in range(len(s1)):
    if s1[i]==s2[i]:s+='0'
    else:s+='1'
print(s)
