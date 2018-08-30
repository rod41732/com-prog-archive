d, m, y = (int(x) for x in input().split())
t = input().strip()
y -= 543
days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if (y%4 == 0 and y%4 != 0) or y%400 == 0:
    days[2] = 29
if y < 2015:
    print("Invalid year")
elif m not in range(1, 12+1):
    print("Invalid month")
elif d > days[m]:
    print("Invalid date")
elif t not in 'EQNF':
    print("Invalid delivery type")
else:
    if t == 'E':
        d += 1
    elif t == 'Q':
        d += 3
    elif t == 'N':
        d += 7
    elif t == 'F':
        d += 14

    if d > days[m]:
        d -= days[m]
        m += 1
    if m > 12:
        m -= 12
        y += 1

    print('delivered on %d/%d/%d'%(d, m, y+543))



