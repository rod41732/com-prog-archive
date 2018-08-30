n = int(input().strip())
n -= 543
print(29 if (n%4 == 0 and n%100 != 0) or n%400 == 0 else 28)