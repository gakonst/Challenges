import math

def isLeapYear(year):
    if year > 1917:
        return True if year%400==0 or (year%4==0 and year%100!=0) else False
    else:
        return True if year%4==0 else False

#print (isLeapYear(2008))

# day = 256 - X
# month = 256 % day
daysWithoutFebruary = 31+31+30+31+30+31+31
year = int(input())


feb = 28
if year==1918:
    feb = 28-14
if isLeapYear(year):
    feb = 29

days = daysWithoutFebruary+feb
day = 256-days
month = math.ceil(days/30)

print ('{:02d}.{:02d}.{}'.format(day,month,year))
