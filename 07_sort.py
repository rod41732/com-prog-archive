# Wasting 24 lines to run in sublime text LUL
################  4HEader #######################
import sys                                      #
debugging, sublime, tofile= 0, 0, 0             #
debugging = 1                                   #
tofile = 1                                      #
sublime = 1                                     #
if sublime:                                     #
	__OMEGALUL__ = open('.test.in', 'r')        #
	input = lambda : __OMEGALUL__.readline      #
if tofile and sublime:                          #
	__LUL3D___ = open('.test.out', 'w')         #
	# sys.stdout = __LUL3D___                   #
def debug(*args):                               #
	if debugging:                               #
		print(*args)                            #
#################################################
#---------------------------------------------------#---------------------------------------------------
def solve_07_V1():
    print('dadbe'[int(input())-1])

#---------------------------------------------------#---------------------------------------------------
def solve_07_V2():
    d = [int(x) for x in input().split()]
    mode = input().strip()
    if mode == 'a':
    	for i in range(len(d)):
    	  for j in range(1,len(d)-i):
    	    if d[j-1] > d[j]:
    	      d[j-1], d[j] = d[j], d[j-1]
    else:
    	for i in range(len(d)):
    	  for j in range(1,len(d)-i):
    	    if d[j-1] < d[j]:
    	      d[j-1], d[j] = d[j], d[j-1]
    print(d)

#---------------------------------------------------#---------------------------------------------------
def solve_07_V3():
    file = open('.data.txt', 'r')
    hotels = []
    min_star = int(input())
    for line in file:
      hotel, star, review = line.split(';')
      if int(star) >= min_star:
        hotels.append([hotel, int(star), float(review), ' '.join(line.strip().split(';'))])
    file.close()

    if hotels:
      print(*(hotel[3] for hotel in sorted(hotels, reverse=True, key=lambda x:x[2])), sep='\n')
    else:
      print("Not Found")

#---------------------------------------------------#---------------------------------------------------
def solve_07_V4(): 
    file = open('.data.txt', 'r')
    today = input().strip()
    od = [] #overdue
    for line in file:
    	book = line.split()
    	if today > book[2]: #book[2] is dueDate
    		od.append(book)
    if not od:
    	print('Not Found')
    else:
    	n = len(od)
    	for k in range(od-1):
    		for i in range(od-1):
    			if od[i][2] > od[i+1][2]:
    				od[i], od[i+1] = od[i+1], od[i]
    	for book in od:
    		print(' '.join(book))
#---------------------------------------------------#---------------------------------------------------
def solve_07_L1():
    print(['j', 'k', 'g', 'tu', 'n'][int(input())-1])
    	
#---------------------------------------------------#---------------------------------------------------
def solve_07_L2():
    ls = [int(x) for x in input().split()]
    for k in range(len(ls)):
    	minIdx = k
    	for i in range(k, len(ls)):
    		if ls[i] < ls[minIdx]:
    			minIdx = i
    	ls[minIdx], ls[k] = ls[k], ls[minIdx]
    print(ls)
#---------------------------------------------------#---------------------------------------------------
def solve_07_L3():
    ls = [int(x) for x in input().split()]
    n = len(ls)
    for k in range(n-1):
    	for i in range(n-1):
    		if ls[i] > ls[i+1]:
    			ls[i], ls[i+1] = ls[i+1], ls[i]
    i1, i2 = (n-1)//2, n//2
    print((ls[i1]+ls[i2])/2)
#---------------------------------------------------#---------------------------------------------------
def solve_07_L4():
    file = open('.data.txt', 'r')
    data = []
    for line in file:
    	pid, name, count = line.strip().split(';')
    	data.append([pid, name, int(count)])

    while True:
    	cmd, a1, a2, a3, *rest = input().split() + ['']*3
    	if cmd == 'Q':
    		print("Bye!")
    		break
    	elif cmd == 'T':
    		for item in data:
    			if item[0] == a1:
    				item[2] += int(a2)
    				print(item)
    				break
    		else:
    			print('Product code does not exist.')
    	elif cmd == 'U':
    		for item in data:
    			if item[0] == a1:
    				item[2] = int(a2)
    				print(item)
    				break
    		else:
    			print('Product code does not exist.')
    	elif cmd == 'A':
    		for item in data:
    			if item[0] == a1:
    				print('Duplicate product code.')
    				break
    		else:
    			newitem = [a1, a2, int(a3)]
    			data.append(newitem)
    			print(newitem)
    	elif cmd == 'D':
    		for idx, item in enumerate(data):
    			if item[0] == a1:
    				data[idx:idx+1] = []
    				print(a1, 'deleted')
    				break
    		else:
    			print('Product code does not exist.')

#---------------------------------------------------#---------------------------------------------------
def solve_07_P1():
    s = input().strip()
    cnt = [0]*10
    for char in s:
    	cnt[int(char)] += 1
    for x in cnt:
    	print(x)
#---------------------------------------------------#---------------------------------------------------
def solve_07_P2():
    s = input().strip()
    cnt = [0]*62
    for i, char in enumerate('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'):
    	for c in s:
    		if c == char:
    			cnt[i] += 1
    print(*cnt)
#---------------------------------------------------#---------------------------------------------------
def solve_07_P3():
    file = open('.data.txt', 'r')
    ls = []
    for line in file:
    	ls.append([int(x) for x in line.split()])
    file.close() 
    while True:
    	x = int(input())
    	if x == -1:
    		break
    	else:
    		for std in ls:
    			if std[0] == x:
    				print(std[1])
    				break
    		else:
    			print('Not Found')
#---------------------------------------------------#---------------------------------------------------
def solve_07_P4():
    ls = []
    while True:
    	x = int(input())
    	if x == -1: 
    		break
    	else: 
    		ls.append(x)
    ls.sort()
    n = len(ls)
    for i in range(n-(n//2)):
    	if ls[i] == ls[i+n//2]:
    		print(ls[i])
    		break
    else:
    	print('Not found')
#---------------------------------------------------#---------------------------------------------------
def solve_07_P5():
    ls = []
    n = int(input())
    for i in range(n):
    	ls.append(int(input()))
    for k in range(n-1):
    	for i in range(n-1):
    		if ls[i] < ls[i+1]:
    			ls[i], ls[i+1] = ls[i+1], ls[i]
    print(*ls, sep='\n')
#---------------------------------------------------#---------------------------------------------------
def solve_07_P6():
    n = int(input())
    a = []
    mean = 0
    for i in range(n):
    	x = int(input())
    	a.append(x)
    	mean += x
    mean /= n
    a.sort()
    med = (a[n//2]+a[(n-1)//2])/2
    mod = modcnt = 0
    for num in a:
    	if a.count(num) > modcnt:
    		modcnt = a.count(num)
    		mod = num
    print(mean, med, mod)
#---------------------------------------------------#---------------------------------------------------
def solve_07_P7():
    file = open('score.txt')
    std = []
    for line in file:
      std.append(int(line.split()[0]))
    std.sort()
    print(*std, sep='\n')
#---------------------------------------------------#---------------------------------------------------
def solve_07_P8():
    file = open('score.txt')
    std = []
    for line in file:
      std.append(int(line.split()[0]))
    std.sort(reverse=True)
    print(*std, sep='\n')
#---------------------------------------------------#---------------------------------------------------
def solve_07_P9():
    ls = [int(x) for x in input().split()]
    odd = sorted([x for x in ls if x%2], reverse=True)
    even = sorted([x for x in ls if x%2 == 0])
    print(*(even + odd))
#---------------------------------------------------#---------------------------------------------------
def solve_07_P10():
    n = int(input())
    ls = [input().strip() for i in range(n)]
    cnt = 0
    for k in range(n-1):
      for i in range(n-1):
        if len(ls[i]) > len(ls[i+1]) or \
        len(ls[i]) == len(ls[i+1]) and ls[i] > ls[i+1]:
          ls[i], ls[i+1] = ls[i+1], ls[i]
          cnt += 1
    for x in ls:
      print(x)
    print(cnt)
#---------------------------------------------------#---------------------------------------------------
def solve_07_P11():
    gl = 'F D D+C C+B B+A'
    gn = [0, 1, 1.5, 2, 2.5, 3, 3.5, 4]
    r, c = [int(x) for x in input().split()]
    for i in range(r):
    	cnt = _sum = 0
    	for g in input().split():
    		if g in gl:
    			cnt += 1
    			_sum += gn[gl.find(g)//2]
    	print("%.2f"%(_sum/cnt))
#---------------------------------------------------#---------------------------------------------------
def solve_07_P12():
    x, n = [int(e) for e in input().split()]
    ans = 0
    a = [[int(x) for x in input().split()] for i in range(n)]
    if x == 0:
    	for i in range(n):
    		for j in range(n):
    			if i >= j:
    				ans += a[i][j]
    if x == 1:
    	for i in range(n):
    		for j in range(n):
    			if i <= j:
    				ans += a[i][j]
    print(ans)
#---------------------------------------------------#---------------------------------------------------
def solve_07_p13():
    r,c = int(input()), int(input())
    a = [input().strip() for i in range(r)]
    for i in range(r):
    	for j in range(i+1, r):
    		if a[i] == a[j]:
    			print(i+1, a[i], j+1, a[j], sep='\n')
#---------------------------------------------------#---------------------------------------------------
def solve_07_P14():
    r, c = [int(e) for e in input().split()]
    a = [[int(e) for e in input().split()] for i in range(r)]
    mr, mc = [], []
    for i in range(r):
    	mn = a[i][0]
    	for j in range(c):
    		if a[i][j] < mn:
    			mn = a[i][j]
    	mr.append(mn)
    for i in range(c):
    	mx = a[0][i]
    	for j in range(r):
    		if a[j][i] > mx:
    			mx = a[j][i]
    	mc.append(mx)
    found = False
    for i in range(r):
    	if found: break
    	for j in range(c):
    		if a[i][j] == mr[i] == mc[j]:
    			print(a[i][j])
    			found = True
    			break
    if not found:
    	print(-1)

#---------------------------------------------------#---------------------------------------------------
def solve_07_P15():
    n = int(input())
    a = [[int(e) for e in input().split()] for i in range(n)]
    for i in range(n):
    	sCol = 0
    	sRow = 0
    	for j in range(n):
    		sCol += a[j][i]
    		sRow += a[i][j]
    	if sRow == 1 and sCol == n:
    		print(i)
    		break
    else:
    	print(-1)
#---------------------------------------------------#---------------------------------------------------
def solve_07_P16():
    r,c = [int(e) for e in input().split()]
    a = [[0]*c for i in range(r)]
    for k in range(2):
    	for i in range(r):
    		t = [int(x) for x in input().split()] #input row
    		for j in range(c):
    			a[i][j] += t[j]
    for i in range(r):
    	print(*a[i])
#---------------------------------------------------#---------------------------------------------------
def solve_07_P17():
    std = []
    while True:
    	inp = [float(e) for e in input().split()]
    	if len(inp) == 2:
    		std.append(inp)
    	else:
    		std.sort(key=lambda x: (-x[1], x[0]))
    		for i in range(len(std)):
    			if std[i][0] == inp[0]:
    				print(i+1)
    				break
    		else:
    			print('Not Found')
    		break
#---------------------------------------------------#---------------------------------------------------
def solve_07_P18():
    n = int(input())
    a = []
    for i in range(n):
    	x = input().strip()
    	a.append([*[x.count(char) for char in 'abcdefghijklmnopqrstuvwxyz'], x])
    a.sort()
    for c in a:
    	print(c[-1])
################## LOOOL 4HEad ##################
if sublime:                                     #
	__OMEGALUL__.close()                        #
if tofile and sublime:                          #
	__LUL3D___.close()                          #
#################################################