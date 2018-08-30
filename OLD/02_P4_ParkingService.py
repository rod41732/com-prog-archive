h1, m1, h2, m2 = [int(input().strip()) for i in range(4)]
diff = (h2*60 + m2)-(h1*60 + m1)
if diff <= 15:
  price = 0
elif diff > 360:
  price = 200
else:
  hour = (diff+59)//60
  price = hour*10
  if hour > 3:
    price += (hour-3)*10
print(price)