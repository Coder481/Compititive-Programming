a = input().split()
n = len(a)

for i in range(1 << n):
    for j in range(n):
        if (i & (1 << j)):
            print(a[j],end =" ")

    print()

# no of subsets of a given set of size "n" is 2**n
# in bits 2**n = 1<<n
print("No. of subsets = ",1<<n)