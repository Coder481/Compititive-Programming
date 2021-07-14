
# Method 1

def invertRightMostSetBit(x):
    a = x
    i = 0

    # find the position of the rightmost set bit
    while (x & 1 == 0):
        i += 1
        x = x >> 1
    
    # invert using Bit Masking
    mask = ~(1 << i)
    a = a & mask

    return a

a = int(input("Enter number to invert rightmost set bit (using method 1): "))
print("Result after inverting rightmost set bit = ",invertRightMostSetBit(a))




# Method 2
'''
The bitwise AND operation of (X) and (X-1) invert the rightmost set bit
'''
def invertRMSetBit(x):
    return x & (x-1)

b = int(input("Enter number to invert rightmost set bit (using method 1): "))
print("Result after inverting rightmost set bit = ",invertRightMostSetBit(b))