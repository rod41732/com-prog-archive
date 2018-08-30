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
a, b,c = [int(x) for x in input().strip().split()]
if a!=0 and(b%a==0 or c%a!=0):
	d = b//a + c%a
else:
	d = int(input())
if d < b:
	b *= 2
	a, c = c, a 
	if b > a+c:
		d += b//2
		c -= 1
if d < b and d%2 == 0:
	a += b-d
	c += 1
elif d == b:
	a -= 1
elif d > a+c:
	b **= 2
else:
	d += b
print(a, b, c, d)

# ---------------- LOOOL 4HEad -----------------
if sublime:
	__OMEGALUL__.close()
if tofile and sublime:
	__LUL3D___.close()
# ----------------------------------------------
