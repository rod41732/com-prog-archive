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
base = int(input())
start, stop, step = [sum(int(digit)*base**i for i, digit in enumerate(x[::-1])) for x in input().strip().split()]
for x in range(start, stop, step):
	out = ''
	while x:
		out = str(x%base) + out
		x //= base
	print(out if out else 0)
# ---------------- LOOOL 4HEad -----------------
if sublime:
	__OMEGALUL__.close()
if tofile and sublime:
	__LUL3D___.close()
# ----------------------------------------------