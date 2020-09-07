for i in range(1,6):
    inp=input().split()    
    if '1' in inp:
        break
j=inp.index('1')+1
ic=0
jc=0
if i<3:
    while True:
        i,ic=i+1,ic+1
        if i==3:
            break
elif i>3:
    while True:
        i,ic=i-1,ic+1
        if i==3:
            break
if j>3:
    while True:
        j,jc=j-1,jc+1
        if j==3:
            break
elif j<3:
    while True:
        j,jc=j+1,jc+1
        if j==3:
            break
print(ic+jc)
