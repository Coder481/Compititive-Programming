n=int(input())
l=[]
for _ in range(n):
    l.append(input())
count=1
for i in range(n):
    try:
        if l[i]==l[i+1]:
            continue
        elif l[i]!=l[i+1]:
            count+=1
    except:
        continue
print(count)
