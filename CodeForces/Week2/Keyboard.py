#https://codeforces.com/contest/474/problem/A
c,s=input(),input()
s1,s2,s3,os='qwertyuiop','asdfghjkl;','zxcvbnm,./',''
if c=='R':
    for e in s:
        if e in s1:
            if s1.index(e)==0:os+=s1[0]
            else:os+=s1[s1.index(e)-1]
        elif e in s2:
            if s2.index(e)==0:os+=s2[0]
            else:os+=s2[s2.index(e)-1]
        elif e in s3:
            if s3.index(e)==0:os+=s3[0]
            else:os+=s3[s3.index(e)-1]
if c=='L':
    for e in s:
        if e in s1:
            if s1.index(e)==len(s1)-1:os+=s1[len(s1)-1]
            else:os+=s1[s1.index(e)+1]
        elif e in s2:
            if s2.index(e)==len(s2)-1:os+=s2[len(s2)-1]
            else:os+=s2[s2.index(e)+1]
        elif e in s3:
            if s3.index(e)==len(s3)-1:os+=s3[len(s3)-1]
            else:os+=s3[s3.index(e)+1]
print(os)
