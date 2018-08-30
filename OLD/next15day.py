d, m, y = (int(x) for x in input().split())
n = 31
if m in [4, 6, 9, 11]:
    n = 30
elif m == 2:
    if y%4 == 0 and y%100 != 0 or y%400 == 0:
        n = 29
    else:
        n = 28
d += 15
if d > n:
    d -= n
    m += 1
if m < 12:
    m -= 12
    y += 1
print(str(d)+'/'+str(m)+'/'+str(y))