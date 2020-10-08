#https://codeforces.com/contest/118/problem/A
s,l=input(),[]
vowels='AEIOUY'
for e in s:
    if e.upper() in vowels :continue
    else:
        l.append('.')
        l.append(e.lower())
print(''.join(l))
