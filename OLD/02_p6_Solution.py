a1, b1, c1 = [int(x) for x in input().strip().split()]
a2, b2, c2 = [int(x) for x in input().strip().split()]
if a1*b2 != a2*b1:
  print('one solution')
else:
  if b1*c2 != b2*c1 or a1*c2 != a2*c1:
    print('no solution')
  else:
    print('many solutions')
