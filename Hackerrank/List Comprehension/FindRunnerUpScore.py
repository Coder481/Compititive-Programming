#https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
n=int(input())
l1=input().split()
l=[]
for e in l1:
    l.append(int(e))
l.sort()
l.reverse()
c=0

for i in range(1,len(l)):
    if l[0]==l[i]:
        l[0]=l[i]
        c+=1
    else:
        print(l[i])
        break
    if c==len(l)-1:
        print(l[0])
