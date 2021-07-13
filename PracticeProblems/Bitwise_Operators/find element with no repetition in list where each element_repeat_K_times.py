import math
a = [12,1,12,3,12,1,1,2,3,3]
k = 3

count = [0] * (int(math.log(max(a),2))+1)

for i in range(len(count)):
    for j in range(len(a)):
        p = a[j]
        p = p >> i
        if (p & 1 == 1):count[i] += 1

count.reverse()

s = ""
for i in range(len(count)):
    s = s + str(count[i]%k)

print(int(s,2))