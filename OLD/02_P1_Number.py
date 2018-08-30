n = int(input().strip())
sign = 'positive' if n > 0 else 'negative' if n < 0 else 'zero'
parity = 'odd' if n%2 == 1 else 'even'
print(sign, parity, sep='\n')