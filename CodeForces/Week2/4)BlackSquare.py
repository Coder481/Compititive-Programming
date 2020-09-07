loc=[int(ele) for ele in input().split()]
s=input()
sum=0
for e in s:
    e=int(e)
    sum+=loc[e-1]
print(sum)
