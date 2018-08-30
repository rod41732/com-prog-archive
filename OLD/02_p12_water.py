amax, a = [int(x) for x in input().strip().split()]
bmax, b = [int(x) for x in input().strip().split()]
b += a; a = 0
if b > bmax:
    a = b-bmax
    b = bmax
print(a, b)
