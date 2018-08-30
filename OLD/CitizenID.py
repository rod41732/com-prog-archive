n = int(input())
_sum = 0
for i in range(12):
    _sum += (i+2)*(n%10)
    n //= 10
print((11-_sum%11)%10)