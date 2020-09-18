#https://codeforces.com/contest/225/problem/A
dice = int(input())
top_of_tower = int(input())
last_top, last_bottom = top_of_tower, 7 - top_of_tower

for i in range(dice):
    sides = list(map(int, input().split()))
    sides += [7 - sides[0], 7 - sides[1]]
    if last_bottom not in sides and last_top not in sides:
        last_bottom, last_top = last_top, last_bottom
    else:
        print("NO")
        exit()

print("YES")
