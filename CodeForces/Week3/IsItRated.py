#https://codeforces.com/contest/807/problem/A
arr1 = []
arr2 = []
for _ in range(int(input())):
    a, b = input().split()
    arr1.append(int(a))
    arr2.append(int(b))

n = len(arr1)

def isItRated(n, arr1, arr2):
    for i in range(0, n):
        if arr1[i] != arr2[i]:
            print("rated")
            return
    for i in range(1,n):
        if arr1[i] > arr1[i-1]:
            print("unrated")
            return

    print("maybe") 

isItRated(n, arr1, arr2)
