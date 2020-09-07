#https://codeforces.com/contest/766/problem/A
a,b=input(),input()
alen,blen,count=len(a),len(b),0
if alen==blen:
    for i in range(alen):
        for j in range(i,blen):
            if a[i]==b[j]:
                count+=1
                break
            else:break
    if count==alen:print('-1')
    else:print(alen)
else:
    print(max(alen,blen))
