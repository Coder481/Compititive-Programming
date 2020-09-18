#https://codeforces.com/contest/287/problem/A
l=[]
for _ in range(4):
    l.append(input())
for i in range(len(l)):
    for j in range(4):
        if j==3 or i==3:break    
        nl,has,dot=[],0,0
        nl+=[l[i][j],l[i][j+1],l[i+1][j],l[i+1][j+1]]
        for e in nl:
            if e=='#':has+=1
            elif e=='.':dot+=1
        if (has==3 and dot==1) or (has==1 and dot==3) or (has==0 and dot==4) or (has==4 and dot==0):
            print('YES')
            exit()    
print('NO')
