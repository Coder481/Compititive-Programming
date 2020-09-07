#https://www.hackerrank.com/challenges/calendar-module/problem
import calendar
n=input()
l=n.split()
o=calendar.weekday(int(l[2]),int(l[0]),int(l[1]))
if o==1:
    print('TUESDAY')
elif o==2:
    print('WEDNESDAY')
elif o==3:
    print('THURSDAY')
elif o==4:
    print('FRIDAY')
elif o==5:
    print('SATURDAY')
elif o==6:
    print('SUNDAY')
elif o==0:
    print('MONDAY')
