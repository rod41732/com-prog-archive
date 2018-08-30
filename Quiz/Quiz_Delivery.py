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
	sys.stdout = __LUL3D___
def debug(*args):
	if debugging:
		print(*args)
# ----------------------------------------------
d, m, y = [int(x) for x in input().strip().split()]
dtype = input().strip()
dim = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
y -= 543
if (y%4==0 and y%100!=0) or y%400==0:
	dim[2] += 1
if y < 2558-543:
	print('Invalid year')
elif not (1 <= m <= 12):
	print('Invalid month')
elif d > dim[m] or d <= 0:
	print('Invalid date')
elif dtype not in 'EQNF':
	print('Invalid delivery type')
else:
	d += 1 if dtype=='E' else 3 if dtype=='Q' else \
	7 if dtype=='N' else 14
	if d > dim[m]:
		d -= dim[m]
		m += 1
		if m == 13:
			m -= 12
			y += 1
	print('delivered on %d/%d/%d'%(d, m, y+543))


# ---------------- LOOOL 4HEad -----------------
if sublime:
	__OMEGALUL__.close()
if tofile and sublime:
	__LUL3D___.close()
# ----------------------------------------------