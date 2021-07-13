# Check that two integrs have opposite sign or not 
# without using any arithmetic operator 

x = int(input())
y = int(input())

print(x," and ",y," have opposite sign? ",((x^y)<0))


# Explanation:
'''
Sign bit of a number is "1" if number is negative
Sign bit of a number is "0" if number is positive

if we perform XOR operation on both numbers, then 
        -> if numbers have different sign bit then XOR value will have "1" as Sign bit (so, XOR value will be negative)
        -> if numbers have same sign bit then XOR value will have "0" as Sign bit (so, XOR value will be positive)
        
Example:
    let x = 2 {sign bit (SX) = 0}
    let y = -2 {sign bit (SY) = 1}
    
    xorValue = x ^ y 
    sign bit of xorValue = 1 
    hence xorValue is negative
    
    So, if two numbers have different sign bit then their XOR value will be negative
'''
