#https://www.hackerrank.com/challenges/word-order/problem
d = dict()
for _ in range(int(input())):
    word = input().strip()
    d[word] = d.get(word,0) + 1

print(len(d))
print(*d.values())
