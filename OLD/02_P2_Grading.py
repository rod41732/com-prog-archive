n = float(input().strip())
if 80 <= n <= 100:
  print('A')
elif 75 <= n < 80:
  print('B+')
elif 70 <= n < 75:
  print('B')
elif 65 <= n < 70:
  print('C+')
elif 60 <= n < 65:
  print('C')
elif 55 <= n < 60:
  print('D+')
elif 50 <= n < 55:
  print('D')
elif 0 <= n < 50:
  print('F')
else:
  print('ERROR')