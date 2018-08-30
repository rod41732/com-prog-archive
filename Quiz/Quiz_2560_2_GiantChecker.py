x = input().strip()
rowerr = colerr = 0 #
if len(x) <= 3:
	col = x[0]
	row = x[1:].strip()
else:
	i1 = x.find('=')
	i2 = x.find(',')
	i3 = x.find('=', i1)
	row = x[i1+1:x2].strip() 
	col = x[i3+1:].strip()
	if x[:3] == col:
		row, col = col, row

if len(col) != 1 or not 'a' <= col.lower() <= 'z':
	colerr = 1
if not row.isdigit() or not(1<=int(row)<=52):
 	rowerr = 1


if rowerr and colerr:
	print('Invalid column and row')
elif rowerr:
	print('Invalid row')
elif colerr:
	print('Invalid column')
else:  
	print(['Black', 'White'][(ord(col)-ord('A')+1+int(row))%2])

