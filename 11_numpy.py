# Wasting 24 lines to run in sublime text LUL
# ------------------ 4Header -------------------
import sys
debugging, sublime, tofile= 0, 0, 0
debugging = 1
tofile = 1
sublime = 1
if sublime:
    __OMEGALUL__ = open('.test.in', 'r')
    input = lambda : __OMEGALUL__.readline()
if tofile and sublime:
    __LUL3D___ = open('.test.out', 'w')
    # sys.stdout = __LUL3D___
def debug(*args):
    if debugging:
        print(*args)
# ----------------------------------------------
def solve_V1():
	print('dbdad'[int(input())-1])
# solve_V1()

def solve_V2():
	from numpy import array as arr
	prices = arr([*map(float, input().split())])
	data = arr([[*map(float, input().split())] for i in range(4)])
	mx = max((sum(data[:, i]), i) for i in range(5))
	print(['Mon', 'Tue', 'Wed', 'Thu', 'Fri'][mx[1]], mx[0])
	print(*(sum(data[:, i]*prices) for i in range(5)))
# solve_V2()


def solve_V3():
	import numpy as np 
	def read_height_weight():
		return np.array([(*map(int ,input().split()),) for i in range(int(input()))])

	def cm_to_m(x):
		return x/100

	def cal_bmi(hw):
		return hw[:, 1]/cm_to_m(hw[:, 0])**2

	def main():
		hw = read_height_weight() 
		# print(hw)
		bmi = cal_bmi(hw) 
		avg_bmi = sum(bmi)/len(bmi) 
		count_underweight = sum(1 for b in bmi if b < 18.5)
		print('average bmi =', avg_bmi)
		print('#bmi < 18.5 =', count_underweight)

	exec(input().strip())
# solve_V3()

def solve_V4():
	import numpy as np
	def read_square_matrix():
		d = [int(e) for e in input().split()]
		m = [d]
		for k in range(len(d)-1):
			m.append([int(e) for e in input().split()])
		return np.array(m)
	
	def min_in_each_row(m):
		return np.array([min(m[i]) for i in range(len(m))])
	def max_in_each_column(m):
		return np.array([max(m[:,i]) for i in range(len(m[0]))])
	  
	def diff_of_sums_of_two_diags(m):
		return sum(m[i][i] for i in range(len(m))) - sum(m[-i-1][i] for i in range(len(m)))

	def halve(m):
		return np.array( [[sum(m[2*i+x%2, 2*j+x//2] for x in range(4))
			for j in range(len(m)//2)] for i in range(len(m)//2)])

	exec(input().strip())# do not remove this line
# solve_V4()

def solve_L1():
	print('acbcb'[int(input())-1])
	# 1) obvious LUL
	# 2) u can use slice as index
	# 3) x.T = x.transpose()
	# 4) numpy.ndenumerate() --> equivalent to enumerate() but fro array
	# 5) axis 0 = vertically(rows), axis-1 = horizontally (cols)
# solve_L1()

def solve_L2():
	import numpy as np
	def all_pair_distances(p):
		# no need to make n*n matrix as 1*n and n*1 matrix will broadcast
		# important to use double bracket as it will make array 2-D
		# [1,2,3].T = [1,2,3]
		# but [[1,2,3]].T = [[1], [2] ,[3]] 
		x = np.array([[p[i][0] for i in range(len(p))]]) 
		y = np.array([[p[i][1] for i in range(len(p))]])
		# 1*n - n*1 --> broadcast array
		dX = x-x.T
		dY = y-y.T
		d = np.sqrt(dX**2 + dY**2)
		return d
	exec(input().strip())
# solve_L2()

def solve_L3():
	import numpy as np
	def eval_poly(x, coeff):
		# make [1, x, x**2, ...]
		powers = x*np.ones(len(coeff))
		powers[0] = 1
		powers = np.cumprod(powers)
		return sum(coeff*powers)
	exec(input().strip())
# solve_L3
def solve_L4():
	import numpy as np
	def checker(n):
		# bitwise XOR EZ Clap
		r = np.array([1-np.cumsum(np.ones(n))%2], int)
		return r^r.T

	def collide(e, c):
		x, y, r = c[:, 0], c[:, 1], c[:, 2]
		return c[(e[0]-x)**2 + (e[1]-y)**2 <= (e[2]+r)**2]

	def matrix_chain_mult(M, order):
		a, b, *rest = order
		mx, mn = max(a, b), min(a, b)
		result = np.matmul(M[a], M[b])
		for idx in rest:
			if idx < mn:
				result = np.matmul(M[idx], result)
			else:
				result = np.matmul(result, M[idx])
			mx, mn = max(mx, idx), min(mn, idx)
		return result
	exec(input().strip())
# solve_L4()

def solve_P1():
	import numpy as np
	from math import e
	data = np.array([[15,3.78],[29,2.0],[10,2.5],[25,2.85],[30,3.96]])
	logit_pi = np.array(-3.98 + 0.2*data[:, 0] + 0.5*data[:, 1])
	p_xi = 1/(1+e**-logit_pi)
	n = int(input())
	if not(1<=n<=5): print('Error')
	else: print(['False', 'True'][p_xi[n-1] > 0.5])
# solve_P1()

def solve_P2():
	from numpy import array, dot
	n = int(input())
	prices = array([float(input().split()[1]) for i in range(n)])
	sales = array([[*map(float, input().split()[1:])] for i in range(n)])
	money = dot(prices, sales) # prices DOT each column of sales
	print(*money, sep='\n') 
# solve_P2()

def solve_P3():
	import numpy as np
	n = int(input())
	[input() for i in range(3)] # waste
	for i in range(n-3):
		print(np.sum(np.array([*map(float, input().split(',')[1:])])))
# solve_P3()

def solve_P4(): #didn't know it is intende to solve using for loop LUL
	import numpy as np
	def pwr(n, k):
		base = np.array([[0, 1],[1, 1]], int)
		if n == 1:
			return base
		elif n == 0:
			return np.identity(2, int)
		h = pwr(n//2, k)
		if n%2 == 1:
			return np.matmul(np.matmul(h, h), base)%k
		else:
			return np.matmul(h, h)%k

	def fib(n, k):
		return pwr(n, k)[0, 1]

	n, k = map(int, input().split())
	print(fib(n, k))
# solve_P4()

def solve_P5():
	import numpy as np
	def pwr(n, k):
		base = np.array([[0, 1],[1, 1]], int)
		if n == 1:
			return base
		elif n == 0:
			return np.identity(2, int)
		h = pwr(n//2, k)
		if n%2 == 1:
			return np.matmul(np.matmul(h, h), base)%k
		else:
			return np.matmul(h, h)%k

	def fib(n, k):
		return pwr(n, k)[0, 1]

	n, k = map(int, input().split())
	print(fib(n, k))
# solve_P5()


def solve_P6():
	import numpy as np
	def scale(img, c):
		row, col = len(img), len(img[0])
		# print(row, col)
		# print(*(img[c*i:c*(i+1), c*j:c*(j+1)] for i in range(row//c) for j in range(col//c)), sep='\n')
		return np.array([[ np.sum(img[c*i:c*(i+1), c*j:c*(j+1)])/c**2 for j in range(col//c)] for i in range(row//c)])

	def read_img():
		row, col = [int(e) for e in input().split()]
		img = np.ndarray((row,col))
		for i in range(row):
			img[i] = [float(e) for e in input().split()]
		return img

	def show_output(out):
		for i in range(out.shape[0]):
			print(" ".join([str(e) for e in out[i]]))

	img = read_img()
	c = int(input())
	out= scale(img, c)
	show_output(out)
# solve_P6()

def solve_P7():
	import numpy as np
	n = int(input())
	m = np.matrix([[float(e) for e in input().split()] for i in range(n)], int)
	for i in range(n-2):
		m = np.sign(np.matmul((np.identity(n)+m), m))
	print(*(' '.join(map(lambda x: str(int(x)), (m[i].A1))) for i in range(n)), sep='\n')

solve_P7()
# ---------------- LOOOL 4HEad -----------------
if sublime:
    __OMEGALUL__.close()
if tofile and sublime:
    __LUL3D___.close()
# ----------------------------------------------