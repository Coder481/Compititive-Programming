#https://www.hackerrank.com/challenges/python-lists/problem
l=[]
for _ in range(int(input())):
    word=input().split()
    w=word[0]
    if w=='print':
        print(l)
    elif len(word)>2:
        digit2,digit1=int(word[2]),int(word[1])
        if w=='insert':
            l.insert(digit1,digit2)
    elif len(word)>1:
        digit=int(word[1])
        if w=='remove':
            l.remove(digit)
        elif w=='append':
            l.append(digit)
    else:
        if w=='sort':
            l.sort()
        elif w=='pop':
            l.pop()
        elif w=='reverse':
            l.reverse()
        
