#https://codeforces.com/contest/742/problem/A
n=int(input())
rem=n%4
if n==0:print('1');exit()
if rem==1:print('8')
elif rem==2:print('4')
elif rem==3:print('2')
elif rem==0:print('6')
