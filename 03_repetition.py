def solve_03_V1():
	print([ 'a', 'p', 'j', 'rs', 'v' ][int(input())-1])

def solve_03_V2():
	n = int(input())
	_sum = 0
	while n > 0:
	    if n%2 == 0:
	        _sum += n
	    n = int(input())
	print(_sum)

def solve_03_V3():
	n = int(input())
	ls = [(x, y) for x in range(n+1) for y in range(n+1) if x < y and x**2+y**2==n]
	for pair in ls:
		print(*pair)
	if not ls:
		print("No solution")
def solve_03_V4():
	x = float(input())
	ans = k = 0
	term = 1
	while abs(term) >= 1e-8:
		ans += term
		term *= -1*x**2/((2*k+1)*(2*k+2))
		k += 1
	print(ans, k-1)

def solve_03_L1():
	print([ 'a', 'p', 'j', 'rs', 'v' ][int(input())-1])

def solve_03_L2():
	n = int(input())
	_sum = 0
	while n > 0:
	    if n%2 == 0:
	        _sum += n
	    n = int(input())
	print(_sum)

def solve_03_V3():
	n = int(input())
	ls = [(x, y) for x in range(n+1) for y in range(n+1) if x < y and x**2+y**2==n]
	for pair in ls:
		print(*pair)
	if not ls:
		print("No solution")
def solve_03_V4():
	x = float(input())
	ans = k = 0
	term = 1
	while abs(term) >= 1e-8:
		ans += term
		term *= -1*x**2/((2*k+1)*(2*k+2))
		k += 1
	print(ans, k-1)


def solve_03_L1():
	print([ 'a', 'v', 'n', 'p', 'efghijklmv' ][int(input())-1])

def solve_03_L2():
	print(int(input().strip(), 2))

def solve_03_L3():
	n, base = [int(x) for x in input().strip().split()]
	if not(2 <= base <= 9) or n < 0:
	    print('Error: Cannot convert')
	else:
	    out = '' 
	    while True: #it's a do-while loop
	        out = str(n%base) + out
	        n //= base
	        if n<=0: 
	        	break
	    print(out)

def solve_03_L4():
	n = int(input())
	print(sum((-1)**i*j*k for i in range(1, n+1) for j in range(1, i+1) for k in range(j, 0, -1)))

def solve_03_P1():
	from math import factorial
	print(factorial(int(input())))
	# print(__import__('functools').reduce(lambda x, y: x*y, range(1,int(input())+1)))

def solve_03_P2():
	from math import factorial
	n, r, x = (int(x) for x in input().strip().split())
	print(factorial(n)//factorial(n-r)//(1 if x == 1 else factorial(r)))

def solve_03_P3():
	print(sum(x for x in range(1, int(input())) if x%3 == 0 or x%5 == 0))

def solve_03_P4():
	n = int(input())
	print(sum([float(input()) for i in range(n)])/n if n else "No Data")

def solve_03_P5():
	ls = []
	x = float(input())
	while x != -1:
		ls.append(x)
		x = float(input())
	print(sum(ls)/len(ls) if ls else "No Data")

def solve_03_P6():
	lim = [0, 50, 55, 60, 65, 70, 75, 80, 101]
	grd = ['Error', 'F', 'D', 'D+', 'C', 'C+', 'B', 'B+', 'A']
	x = int(input())
	while x != -1:
		print(next((g for l,g in zip(lim, grd) if x<l),'Error'))
		x = int(input()) 

def solve_03_P7():
	n, x = (int(e) for e in input().split())
	print(sum(1 for _ in range(n) if int(input()) == x))

def solve_03_P8():
	n = int(input())
	for c in range(n, 0, -1):
		if any(i**2+(n-c-i)**2 == c**2 for i in range(1,n-c)):
			print(c)
			break

def solve_03_P8_2(): # -> Get PPPPPPPPTP WutFace
	n = int(input())
	print([c for c in range(n, 0, -1) if any(i**2+(n-c-i)**2 == c**2 for i in range(1,n-c))][0])
			
def solve_03_P9():
	a, b, c, x, d = [float(x) for x in input().strip().split()]
	n = 1
	fx = a*x**2 + b*x + c
	fpx = 2*a*x + b
	while abs(fx/fpx) >= d:
	    n += 1
	    x = x - fx/fpx
	    fx = a*x**2 + b*x + c
	    fpx = 2*a*x + b
	print(n)

def solve_03_P10():
	n = int(input())
	ls = [i for i in range(n-1, 1, -1) if n%i == 0]
	print(' '.join(map(str,ls)) if ls else "Prime Number")

def solve_03_P11():
	n = int(input())
	ls = []
	for i in range(2, n+1):
	    if not any(i%j == 0 for j in ls):
	        ls.append(i)
	print("input unavailable" if n < 0 else 'none' if not ls else ' '.join(map(str, ls)))


def solve_03_P12():
	n = int(input())
	ls = []
	for i in range(2, n+1):
	    if not any(i%j == 0 for j in ls) and n%i == 0:
	        ls.append(i)
	print(*ls)

def solve_03_P13():
	r, c = [int(x) for x in input().strip().split()]
	print(*(' '.join([str(i*j) for j in range(1, c+1)]) for i in range(1, r+1)), sep='\n')

def solve_03_P14():
	n, t = [int(x) for x in input().strip().split()]
	func = [lambda x,y: x<=y, lambda x,y: x>=y, lambda x,y: x+y==n+1][t-1]
	for i in range(1, n+1):
		for j in range(1, n+1):
			if func(i,j): print('(%d,%d)'%(i, j))

def solve_03_P15():
	n = int(input())
	ls = ['.'*i + '#'*(n-2*i) + '.'*i + '.' + '.'*i + '#'*(n-2*i) + '.'*i for i in range(n//2-1, -1, -1)] \
	 	 + ['#'*(2*n+1)]*(n//2-2) 	+ ['.'*i + '#'*(2*n+1-2*i) + '.'*i for i in range(n+1)] 
	print(*ls, sep='\n')

def solve_03_P15(): # -> ONE LINE
	print(*(list(['.'*i + '#'*(n-2*i) + '.'*i + '.' + '.'*i + '#'*(n-2*i) + '.'*i for i in range(n//2-1, -1, -1)] + ['#'*(2*n+1)]*(n//2-2) + ['.'*i + '#'*(2*n+1-2*i) + '.'*i for i in range(n+1)] for n in [int(input())])[0]), sep='\n') 

def solve_03_P16():
	x, y = int(input()), int(input())
	print(*["%d %d %d"%(x, i, x*i) for i in range(y+1)], sep='\n')