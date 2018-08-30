def solve_06_V1():
	answers = [ 'x', 'k', 'tu', 'c', 'h' ]
	n = int(input())
	print(answers[n-1].lower())

def solve_06_V2():
	fname = input().strip()
	file = open(fname, 'r')
	ans = []
	for line in file:
		data = line.strip().split(';')
		item = list()
		item.append(data[0])
		item.append(data[1] + ' ' + data[2])
		score = float(data[3]) + float(data[4])
		grade = 'A' if score>=80 else 'B' if score>=70 else 'C' if score>=60 else 'D' if score>=50 else 'F'
		item.append(grade)
		ans.append(item)
	print(ans)



def solve_06_V3():
	fname = input().strip()
	file = open(fname, 'r')
	std_data = []
	std_list = []
	for line in file:
		if line.strip() != '':
			data = line.strip().split(';')
			if data[0] not in std_list:
				std_list.append(data[0])
				item = list()
				item.append(data[0])
				item.append(data[1] + ' ' + data[2])
				score = float(data[3]) + float(data[4])
				grade = 'A' if score>=80 else 'B' if score>=70 else 'C' if score>=60 else 'D' if score>=50 else 'F'
				item.append(grade)
				std_data.append(item)
	while True:
		ID = input().strip()
		if ID == '-1':
			break
		for std in std_data:
			if std[0] == ID:
				print(std)
				break
		else:
			print('Not Found')
	file.close()



def solve_06_V4():
	file = open(input().strip(), 'r')
	data = []
	for line in file:
		fruit, person = line.strip().split()
		for item in data:
			if item[0] == fruit:
				item[1].append(person)
				break
		else:
			data.append([fruit, [person]])
	favcnt, favFruit = 0, ''
	for fruit in data:
		if len(fruit[1]) > favcnt:
			favcnt = len(fruit[1])
			favFruit = fruit[0]
	print(data)
	print("The most favorite fruit is", favFruit)



def solve_06_L1():
	answers = [ 'c', 'b', 'b', 'd', 'c' ] 
	n = int(input())
	print(answers[n-1].lower())



def solve_06_L2():
	inp = [int(x)%2 for x in input().strip().split()]
	print(inp, sum(inp))



def solve_06_L3():
	seq = [int(x) for x in input().strip().split()]
	if seq[1] - seq[0] == seq[2] - seq[1] == seq[3] - seq[2]:
		print(seq[-1]+seq[-1]-seq[-2])
	else:
		print(seq[-2]+(seq[-2]-seq[-4]))



def solve_06_L4():
	data = []
	x = input().strip()
	data.append([int(e) for e in x.split()])
	row = len(data[0])//2+1
	for i in range(row-1):
		data.append([int(e) for e in input().strip().split()])
	center = len(data[0])//2
	row = len(data[0])//2+1
	ans = 0
	for i in range(row):
		ans += sum(data[i][center-i:center+i+1])
	print(ans)




def solve_06_P1():
	data = []
	while True:
		x = int(input().strip())
		if x >= 0:
			data.append(x)
		else:
			for i in range(len(data)):
				data[i] += x
			break
	for x in data:
		print(x)



def solve_06_P2():
	n = int(input())
	data = []
	for i in range(n):
		data.append(int(input().strip()))
	x, y = [int(x) for x in input().strip().split()]
	print(sum(data[x:y+1]))



def solve_06_P3():
	n = int(input().strip())
	print(sum([int(x) for x in input().strip().split()])/n)



def solve_06_P4():
	data = [int(x) for x in input().strip().split()]
	idx = -1
	for i in range(len(data)):
		if data[i] < 0:
			idx = i
			break
	print(sum(data[:idx])/idx)



def solve_06_P5():
	while True:
		x = [int(x) for x in input().strip().split()]
		if len(x) == 1:
			break
		else:
			h = x[1]/100
			print(x[0]/h**2)



def solve_06_P6():
	data = [int(x) for x in input().strip().split()]
	avg = []
	for i in range(len(data)):
		part = data[max(i-1, 0): i+2]
		avg.append(sum(part)//len(part))
	print(*avg)



def solve_06_P7():
	v1 = [int(x) for x in (input().strip())[1:-1].split(',') ]
	v2 = [int(x) for x in (input().strip())[1:-1].split(',') ]
	print(sum(v1[i]*v2[i] for i in range(len(v1))))



def solve_06_P8():
	n = int(input())
	data = [i for i in range(1, n+1)]
	while True:
		x, y = [int(x) for x in input().strip().split()]
		if x == y == 0:
			break
		else:
			idx1 = data.index(x)
			idx2 = data.index(y)
			data[idx1], data[idx2] = data[idx2], data[idx1]
	print(data)

def solve_06_P9():
	data = input().strip().split()
	sequence = [int(x) for x in input().strip().split()]
	data = [data[sequence[i]] for i in range(len(sequence))] # can also use same name (data)
	print(*data)


def solve_06_P10():
	# data = [int(x) for x in input().strip().split(', ')]
	# ans = sum(1 for i,x in enumerate(data) if x < 0 and data[i+1] >= 0)
	# print(ans)

	# one liner btw HAhaa
	print([sum(1 for i,x in enumerate(data) if x < 0 and data[i+1] >= 0) for data in [[int(x) for x in input().strip().split(', ')]]][0])	


def solve_06_P11():
	rocks = [int(x) for x in input().strip().split()]
	score = [0]*2
	curr = 0
	while rocks != []: # or we can write just--> while rocks:
		if rocks[-1] > rocks[0]:
			score[curr] += rocks[-1]
			rocks = rocks[:-1]
		else:
			score[curr] += rocks[0]
			rocks = rocks[1:]
		curr = 1-curr
	print("%d\n%d\n%d"%(score[0], score[1], 1 if score[0] > score[1] else 2 if score[0] < score[1] else 0))


def solve_06_P12():
	que = list(input().strip())
	n = int(input().strip())
	for i in range(n):
		cmd = input().strip().split()
		if cmd[0] == 'out':
			del que[int(cmd[1])]
			# OR que = que[0:idx] + que[idx+1:]
		elif cmd[0] == 'in':
			idx = int(cmd[2])
			que[idx:idx] += [cmd[1]]
		else: # SWAP
			id1, id2 = int(cmd[1]), int(cmd[2])
			que[id1], que[id2] = que[id2], que[id1]
		print(''.join(que))


def solve_06_P13():
	n = int(input())
	next_of = [int(input()) for i in range(1, n+1)]
	ans = [1]
	while len(ans) < n:
		ans.append(next_of[ans[-1]-1])
	print(*ans)

def solve_06_P14():
	books = []
	while True:
		cmd = input().strip().split()
		# print(cmd)
		if cmd[0] == 'list':
			print(books)
		elif cmd[0] == 'return':
			books.append(' '.join(cmd[1:]))
			print(len(books)) 
		elif cmd[0] == 'shelf':
			if len(books):
				print(books[-1])
				books = books[:-1]
			else:
				print('no book')
		elif cmd[0] == 'top':
			if len(books):
				print(books[-1])
			else:
				print('no book')
		elif cmd[0] == 'end':
			break