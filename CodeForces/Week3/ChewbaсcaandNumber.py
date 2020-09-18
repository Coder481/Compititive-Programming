#https://codeforces.com/contest/514/problem/A
s,strt=input(),0
l=[int(ele) for ele in s]
if l[0]==9:strt=1
for i in range(strt,len(l)):
    if l[i]>4:
        l[i]=9-l[i]
s=''
for e in l:
    s+=str(e)
print(s)
