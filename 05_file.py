def solve_05_V1():
	answers = [ 'a', 'b', 'e', 'd', 'd' ]
	n = int(input())
	print(answers[n-1].lower())
	# Notes
	"""
	file read -> has new line at the end (from the file)
	file write -> doesn't write \n automatically like print
	"""

def solve_05_V2():
	f = open('data.txt', 'r')
	n = int(input().strip())
	cnt = 0
	for line in f:
		line.strip()
		if 'Name:' in line:
			cnt += 1
		if cnt == n:
			print(line[6:])
			break
	else:
		print('Not Found')
	f.close()

def solve_05_V3():
	filename = input().strip()
	found_id = ""
	f = open(filename, 'r')
	for line in f:
		if line[:10] not in found_id:
			found_id += line[:10] + ';'
			print(line[:10])
	f.close()

def solve_05_V4():
	filename, a, b, c = (input().strip() for i in range(4))
	f = open(filename, 'r')
	data = f.read()
	ca, cb, cc = (sum(1 for x in data if x == key) for key in (a, b, c))
	if ca < cb:
		ca, cb, a, b = cb, ca, b, a
	if cb < cc:
		cc, cb, c, b = cb, cc, b, c
	if ca < cb:
		ca, cb, a, b = cb, ca, b, a
	print(a+b+c)

def solve_05_P1():
	answers = [ 'd', 'c', 'd', 'd', 'd' ]
	n = int(input())
	print(answers[n-1].lower())

def solve_05_L2():
	file = open('data.txt', 'r')
	n = int(input().strip())
	cnt, _sum = 0, 0
	for line in file:
		ld = line.strip().split(':')
		if int(ld[2]) == n:
			cnt += 1
			_sum += float(ld[3])

def solve_05_L3():
	f = open(input().strip())
	c_sum = 0
	for line in f:
		for c in line:
			c_sum = c_sum ^ ord(c)
	f.close()
	print(c_sum)

def solve_05_L4():
	file = open(input().strip())
	n, x, y = int(input().strip()), input(), input()
	if x[-1] in '\r\n': x = x[:-1]
	if y[-1] in '\r\n': y = y[:-1]

	cnt = 0
	for line in file:
		if line[-1] in '\r\n': line = line[:-1]
		linel, xl = line.lower(), x.lower() # case insensitive search
		last = 0
		out = ''
		while True:
			ind = linel.find(xl, last) # case insensitive search
			if ind == -1:
				break
			out += line[last:ind]
			if cnt < n:# case insensitive search
				out += y
				cnt += 1
			else:
				out += line[ind:ind+len(x)]
			last = ind+len(x)
		out += line[last:]
		print(out)

def solve_05_P1():
	file = open(input().strip(), 'r')
	for line in file:
		line = line.strip().split()
		score = sum(int(x) for x in line[-5:])
		if score >= 80:
			grade = 'A'
		elif score >= 75:
			grade = 'B+'
		elif score >= 70:
			grade = 'B'
		elif score >= 65:
			grade = 'C+'
		elif score >= 60:
			grade = 'C'
		elif score >= 55:
			grade = 'D+'
		elif score >= 50:
			grade = 'D'
		else:
			grade = 'F'
		print(line[0], grade)

def solve_05_P2():
	file = open(input().strip(), 'r')
	n = int(file.readline().strip())
	for i in range(n):
		line = file.readline()
		line = line.strip().split()
		score = sum(int(x) for x in line[-5:])
		if score >= 80:
			grade = 'A'
		elif score >= 75:
			grade = 'B+'
		elif score >= 70:
			grade = 'B'
		elif score >= 65:
			grade = 'C+'
		elif score >= 60:
			grade = 'C'
		elif score >= 55:
			grade = 'D+'
		elif score >= 50:
			grade = 'D'
		else:
			grade = 'F'
		print(line[0], grade)

def solve_05_P3():
	file = open('score.txt', 'r')
	ID = input().strip()
	for line in file:
		line = line.strip().split()
		if line[0] == ID:
			print(line[1])
			break
	else:
		print('Not Found')


def solve_05_P4():
	file = open(input().strip(), 'r')
	c = [0, 0, 0, 0, 0]
	ID = ['be', 'se', 've', 'et']
	for line in file:
		line = line.strip().lower().split()
		for i, e in enumerate(ID):
			if e == line[0]:
				c[i] += 1
				c[-1] += 1
	print(*c)


def solve_05_P5():
	f1, f2 = open(input().strip(), 'r'),  open(input().strip(), 'r')
	for l1 in f1:
		l1.strip()
		l2 = f2.readline().strip()
		if l2 in l1:
			print('True') 
		else:
			print('False')	
	print(_sum/cnt if cnt else "Not Found")

def solve_05_P6():
	f1, f2 = open(input().strip(), 'r'),  open(input().strip(), 'r')
	for l1 in f1:
		n = int(l1.strip())
		print(sum(float(f2.readline().strip()) for i in range(n))/n)


def solve_05_P7():
	with open(input().strip(), 'r') as file:
		mode = file.readline().strip()
		key =  file.readline().strip()
		out = ''
		for line in file:
			line = line.strip().split()
			text, st, en = line[0], int(line[1]), int(line[2])
			if mode == 'rfind':
				lp = text.rfind(key, st, en)
			else:
				lp = text.find(key, st, en)

			if lp == -1:
				print('not found')
			else:
				out = key
				rp = lp+len(key)
				if rp < len(text):
					out += text[rp]
				if lp-1 >= 0:
					out = text[lp-1] + out
				print(out)

def solve_05_P8():
	with open(input().strip(), 'r') as file:
		mode = file.readline().strip()
		key =  file.readline().strip()
		out = ''
		for line in file:
			line = line.strip().split()
			text, st, en = line[0], int(line[1]), int(line[2])
			if mode == 'rfind':
				lp = text.rfind(key, st, en)
			else:
				lp = text.find(key, st, en)

			if lp == -1:
				print('not found')
			else:
				out = key
				rp = lp+len(key)
				if rp < len(text):
					out += text[rp]
				if lp-1 >= 0:
					out = text[lp-1] + out
				print(out)
