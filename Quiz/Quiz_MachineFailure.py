fname,n = input().strip(), int(input())
file = open(fname, 'r')
last = ['']*5
found = 0
for line in file:
  for i in range(4):
    last[i] = last[i+1]
  data = line.strip().split(';')
  last[4] = data[1]+';'+data[2]
  if data[2] == 'Failure':
    found = 1
    break
if found == 0:
  print('Not Found')
else:
  for i in range(4-n, 5):
     if last[i]:
       print(last[i])
file.close()