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
dna, op = input().strip().upper(), input().strip()
for x in dna:
	if x not in 'ATCG':
		print('Invalid DNA')
		break
else:
	if op == 'R':
		out = ''
		convert = [['A', 'T'], ['T', 'A'], ['C', 'G'], ['G', 'C']]
		for c in dna[::-1]:
			for x in convert:
				if c == x[0]:
					out += x[1]
		print(out)
	elif op == 'F':
		print(', '.join(['%c=%d'%(char, sum(1 for c in dna if c == char)) for char in 'ATGC']))
	elif op == 'D':
		x = input().strip()
		print(sum(1 for i in range(len(dna)-1) if dna[i:i+2] == x))
# ---------------- LOOOL 4HEad -----------------
if sublime:
	__OMEGALUL__.close()
if tofile and sublime:
	__LUL3D___.close()
# ----------------------------------------------