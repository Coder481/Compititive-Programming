#https://codeforces.com/contest/1237/problem/A
import math as ma
x= int(input())
a = []
o = []
e = []
t = []
for i in range (x):
	p = int(input())
	a.append(p)
	if p%2 ==0:
		e.append(p)
	else:
		o.append(p)
		t.append(p//2)
r = int(abs(sum(e)/2 + sum(t)))
for i in a:
	if i % 2 ==0:
		print(int(i/2))
	else:
		if(r!=0):
			print(ma.ceil(i/2))
			r-=1
		else:
			print(i//2)
