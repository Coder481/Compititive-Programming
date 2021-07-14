'''
4**0 = 1 -> True
4**1 = 4 = 100 
4**2 = 16 = 10000 
4**3 = 64 = 1000000

Number of 0 bit after first set bit are always even if the number is power of 4
'''

def powerOfFour(x):
    i = 0
    if x == 0 : return False
    elif x == 1: return True

    while (x & 1 == 0):
        i += 1
        x = x >> 1
    
    if (i==0):return False
    if (i & 1 == 0):return True
    else : return False

a = int(input())
print(powerOfFour(a))