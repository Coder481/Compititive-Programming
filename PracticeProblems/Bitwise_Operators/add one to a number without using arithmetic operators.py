# Method 1:
'''
We know that negation of a number is represented in 2's compliment
and 2's compliment is find by (~X)+1

So, let a number is X and, we know that    (~X)+1 = -X
after simplification                        X+1 = -(~X)
hence, 1 can be added to a number (X) just by applying -(~X).  
'''

def addOne1(a):
    return -(~a)

a = int(input("Enter any number to add one to it (using Method 1): ")) 
print("Result after adding one = ",addOne1(a)) 



# Method 2:
'''
let a number X = 1001100100111
Now invert all the bits after rightmost 0 bit (here, 4th bit from right)
and also invert the rightmost 0 bit also

we get, X = 1001100101000
'''

def addOne2(x):
    a = x
    i = 0

    # loop till we get rightmost 0 bit 
    while (x & 1 == 1):

        # inverting set bit using Bit Masking
        mask = ~(1 << i)
        a = a & mask

        # right shifting x to get the set bit at the last position
        x = x >> 1

        # changing i to inverting the set bit
        i += 1

    # fliping the rightmost 0 bit  (in above example, 4th bit from right)
    mask = 1 << i
    a = a | mask

    return a

a = int(input("Enter any number to add one to it (using Method 2): "))
print("Result after adding one = ",addOne2(a))