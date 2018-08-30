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

	
	