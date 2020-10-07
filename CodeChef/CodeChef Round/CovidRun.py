#codechef.com/OCT20B/problems/CVDRUN
for _ in range(int(input())):
        n, k, x, y = map(int,input().split())
        i = 0
        while i <= n*2:         
            if x == y:
                print("YES")
                break
            x = (x+k) % n
            i = i + 1
        else: print("NO")
