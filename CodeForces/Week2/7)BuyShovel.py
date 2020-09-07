#https://codeforces.com/contest/732/problem/A
k,r=input().split()
k=int(k)
for i in range(1,11):
    k=int(k)
    k*=i
    s=str(k)
    if s[len(s)-1]==r or k%10==0:
        break
    k/=i
print(i)
