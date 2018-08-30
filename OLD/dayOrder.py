dayBefore = 0
d, m, y = int(input()), int(input()), int(input())
y -= 543
if m > 1:
    dayBefore += 31
if m > 2:
    dayBefore += 28
    if (y%4 == 0 and y%100 != 0) or y%400 == 0:
        dayBefore += 1
if m > 3:
    dayBefore += 31
if m > 4:
    dayBefore += 30
if m > 5:
    dayBefore += 31
if m > 6:
    dayBefore += 30
if m > 7:
    dayBefore += 31
if m > 8:
    dayBefore += 31
if m > 9:
    dayBefore += 30
if m > 10:
    dayBefore += 31
if m > 11:
    dayBefore += 30
print(dayBefore+d)