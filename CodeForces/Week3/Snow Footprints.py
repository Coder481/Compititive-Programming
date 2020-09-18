#https://codeforces.com/contest/298/problem/A
n=int(input())
s,l,rl,ll=input(),[],[],[]
if 'L' not in s:
    for r in s:
        if r=="R":rl.append(s.index(r))
    print(rl[0]+1,len(rl)+rl[0]+1)
    exit()
if 'R' not in s:
    for k in s:
        if k=="L":ll.append(s.index(k))
    print(len(ll)+ll[0],ll[0])
    exit()
for e in s:
    if e=='R':
        l.append(s.index(e))
    if e=='L':
        l.append(s.index(e))
        break
print(l[0]+1,l[len(l)-1])
