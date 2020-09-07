n=int(input())
s=input()
l=list(s)
count=0
for i in range(0,n):
    try:
        if l[i]==l[i+1]:
            l[i]='.'
            count+=1
    except:
        pass
print(count)
