# 1 Vaccine Production
'''import math as m

d1,v1,d2,v2,p = map(int,input().split())
if d1 == d2:
    print(m.ceil(p/(v1+v2)) + (d1-1) )
    exit()
days = min(d1,d2)-1
vac=0
if d1>d2:
    for i in range(d2,d1):
        vac += v2 
        days += 1
        if vac >= p:print(days);exit()
    
    while True:
        vac += (v1+v2)
        days += 1
        if vac >= p:print(days);exit()
else:
    for i in range(d1,d2):
        vac += v1 
        days += 1
        if vac >= p:print(days);exit()

    while True:
        vac += (v1+v2)
        days += 1
        if vac >= p:print(days);exit()'''

# 2 Even Pair Sum
'''import math as m

for _ in range(int(input())):
    a,b=map(int,input().split())
    if b%2==0:
        print(int(a*(b/2)))
        
    else:
        if a%2==0:
            ansE = (a/2)*(m.floor(b/2))
            ansO = (a/2)*(m.ceil(b/2))
            print(int(ansE+ansO))
            
        else:
            ansE = (m.floor(a/2))*(m.floor(b/2))
            ansO = (m.ceil(a/2))*(m.ceil(b/2))
            print(int(ansE+ansO))'''

# 3 Vaccine Distribution
'''import math as m

for _ in range(int(input())):
    n,d = map(int,input().split())
    l = [int(ele) for ele in input().split()]
    risky = sum(map(lambda i: i>=80 or i<=9, l))    
    riskyDays = m.ceil(risky/d)
    normalDays = m.ceil((len(l)-risky)/d)
    print(riskyDays+normalDays)'''
