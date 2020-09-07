try:
    n=int(input())  
    s=input()
    Anton=0
    Danik=0
    for e in s:
        if e=='A':
            Anton+=1
        elif e=='D':
            Danik+=1
    if Anton>Danik:
        print('Anton')
    elif Danik>Anton:
        print('Danik')
    else:
        print('Friendship')
except Exception:
    pass
