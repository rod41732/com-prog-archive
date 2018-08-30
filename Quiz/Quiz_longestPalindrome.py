num, k = [int(x) for x in input().strip().split()]
res = num%10**k
if res//10**(k-1) < 5:
  num -= res
elif res//10**(k-1) > 5:
  num += 10**k-res
else:
  if num//10**k%2 == 1:
    num += 10**k-res
  else:
    num -= res
print(num)