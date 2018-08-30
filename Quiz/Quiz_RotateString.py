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
mode, row = input().strip(), int(input().strip())
data = [input().strip() for i in range(row)]
print('Invalid size' if any(len(data[i]) != len(data[i-1]) for i in range(1, row)) else \
	 *(''.join(x) for x in zip(*data[::-1])) if mode=='90' else \
    (line[::-1] for line in data[::-1]) if mode =='180' else \
    (line[::-1] for line in data), sep='\n') 
# ---------------- LOOOL 4HEad -----------------
if sublime:
	__OMEGALUL__.close()
if tofile and sublime:
	__LUL3D___.close()
# ----------------------------------------------