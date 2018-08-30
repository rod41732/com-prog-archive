m, y = [int(x) for x in input().strip().split()]
y -= 543
days = [0, 31, 29 if (y%4 == 0 and y%100 != 0) or y%400 == 0 else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
print(days[m])
