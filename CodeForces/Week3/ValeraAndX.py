#https://codeforces.com/contest/404/problem/A
n,arr1,arr2=int(input()),[],[]
for i in range(n):
    s=input()
    for j in range(len(s)):
        if i==j or j==n-1-i:arr1.append(s[j])
        else:arr2.append(s[j])
if len(set(arr1))==1==len(set(arr2)) and set(arr1)!=set(arr2):print('YES')
else:print('NO')
