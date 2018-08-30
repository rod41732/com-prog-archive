a, b, c = [int(x) for x in input().strip().split()]
print('NO' if (a+b <= c or b+c <= a or c+a <= b) else 'YES')