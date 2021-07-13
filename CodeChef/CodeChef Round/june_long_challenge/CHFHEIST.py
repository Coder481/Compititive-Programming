
for _ in range(int(input())):
    D,d,P,Q = map(float,input().split())
    
    N = D//d
    n = N * d
    
    ans1 = (N*d)*( (2*P)+((Q*(N-1))) )
    ans2 = (D-n)*( P+(N*Q) ) * 2
    
    finalAns = (ans1 + ans2)/2
    
    temp = int(finalAns)
    if temp == finalAns:
        print(temp)
    else:
        print(finalAns)