def solve_TTT(): # Quiz 1
    x1,x2,x3 = [input().strip() for i in range(3)]
    x = x1+x2+x3
    if len(x) != 9:
        print("ERROR")
    else:
        win = '-'
        for i in range(3):
            if x[3*i] == x[3*i+1] == x[3*i+2]:
                win = x[3*i]
                break
            elif x[i] == x[i+3] == x[i+6]:
                win = x[i]
                break
        if win != '-':
            if x[0] == x[4] == x[8]:
                win = x[0]
            elif x[3] == x[4] == x[6]:
                win = x[3]
    if win == '-':
        print('???')
    else:
        print(win)


def solve_GaintChecker(): #Quiz 2
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
	if row=='' or any(c not in '0123456789' for c in row) or not(1<=int(row)<=52):
	 rowerr = 1
	
	if rowerr and colerr:
		print('Invalid column and row')
	elif rowerr:
		print('Invalid row')
	elif colerr:
		print('Invalid column')
	else:
		print(['Black', 'White'][(ord(col)-ord('A')+1+int(row))%2])


def solve_TextFormatting(): #Quiz 3
	f = open(input().strip())
	k = int(input())
	print(''.join('-'*9 + str(i) for i in range(1, k//10+1)) + '-'*(k%10)) 
	data = f.read().replace('\n', '.') + '.' #read all
	ld = len(data)
	ind = 0; out = ''
	while ind!=-1 and ind<ld: 
		if data[ind] == '.':
			out += '.'
		else:
			ind2 = data.find('.', ind)
			out += data[ind:ind2]
			if len(out) > k:
				if out.strip('.') == data[ind:ind2]: 
					print(out.strip('.'))
					out = ''
				else:
					print(out[:-(ind2-ind)].strip('.'))
					out = data[ind:ind2]
			ind = ind2-1
		ind += 1
	print(out.strip('.'))

		
		