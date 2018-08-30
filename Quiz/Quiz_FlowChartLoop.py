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
op = input().strip()
if op == 'A':
	m, p, q = [int(input()) for i in range(3)]
	for i in range(m+1):
		for j in range(p):
			if i+j > q:
				print("P3", i, j)
				break
		else:
			print("P4", i, j) #???

elif op == 'B':
	m, p  = [int(input()) for i in range(2)]
	i = c = 0
	while i <= m:
		j = i
		while j <= p:
			print(i, j)
			c += 1
			j += 1
		i += 1
	print(c)
else:
	print('Invalid op')
# ---------------- LOOOL 4HEad -----------------
if sublime:
	__OMEGALUL__.close()
if tofile and sublime:
	__LUL3D___.close()
# ----------------------------------------------