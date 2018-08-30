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
c = input().strip()
if c == 'S':
	m = int(input())
	q,r,t,k,n,x,i,p = 1,0,1,1,3,3,0,''
	while i<m:
		if 4*q + r - t < n*t:
			p = p+str(n)
			i += 1
			a = 10*(r - n*t)
			n = 10*(3*q + r)//t - 10*n #???
			q *= 10
			r = a
		else:
			a = (2*q + r)*x
			b = (7*q*k + 2 + x*r)//(x*t)
			q *= k
			t *= x
			x += 2
			k += 1
			n = b
			r = a
	print('pi =', p[0]+'.'+p[1:])
elif c == 'R':
	n = int(input())
	p = round(12**0.5 * sum((-3)**-k/(2*k+1) for k in range(n+1)), 12)
	print('pi =', p)
elif c == 'P':
	p = round((7+(6+(5)**0.5)**0.5)**0.5, 6)
	print('pi =', p)
else:
	print('Invalid')
# ---------------- LOOOL 4HEad -----------------
if sublime:
	__OMEGALUL__.close()
if tofile and sublime:
	__LUL3D___.close()
# ----------------------------------------------