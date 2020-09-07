try:
    n=int(input())
    output=0
    for _ in range(n):
        p,v,t=input().split()
        p,v,t=int(p),int(v),int(t)
        if p+v+t>=2:
            output+=1
    print(output)
except:
    pass
