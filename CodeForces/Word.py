s=input()
l='abcdefghijklmnopqrstuvwxyz'
L=l.upper()
lc,Lc=0,0
for e in s:
    if e in l:lc+=1
    elif e in L:Lc+=1
if lc>=Lc:print(s.lower())
elif lc<Lc:print(s.upper())
