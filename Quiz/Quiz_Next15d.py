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
dim = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
y -= 543
if (y%4==0 and y%100 !=0) or y%400 == 0:
	dim[2] += 1
d += 15
if d > dim[m]:
	d -= dim[m]
	m += 1
	if m == 13:
		m = 1
		y += 1
y += 543
print('%d/%d/%d'%(d, m, y))
# ---------------- LOOOL 4HEad -----------------
if sublime:
	__OMEGALUL__.close()
if tofile and sublime:
	__LUL3D___.close()
# ----------------------------------------------