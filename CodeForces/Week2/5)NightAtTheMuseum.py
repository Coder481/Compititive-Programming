s = input()
pointer = 'a'
ans = 0
for i in s :
    m1 = 26-(abs(ord(pointer) - ord(i)))
    m2 = abs(ord(pointer) - ord(i))
    if m1 < m2 :
       ans += m1
    else:
       ans += m2
    pointer = i
print(ans)
