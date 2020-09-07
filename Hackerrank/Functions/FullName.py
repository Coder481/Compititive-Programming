#https://www.hackerrank.com/challenges/whats-your-name/problem
def print_full_name(a, b):
    b+='!'
    print("Hello",a,b,'You just delved into python.')
first,last=input(),input()
print_full_name(first,last)
