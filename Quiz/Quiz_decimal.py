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
n = input()
if n == '0':
	print('0 = 0')
else:
	data = []
	sign = ' + '
	if n[0] == '-':
		n = n[1:]
		sign = ' - '
	for i, e in enumerate(n[::-1]):
		if e != '0':
			data = ['%c*%d'%(e, 10**i)] + data
	out = sign.join(data)
	if sign == ' - ':
		print('-%s = -%s'%(n, out))
	else:
		print('%s = %s'%(n, out))
# ---------------- LOOOL 4HEad -----------------
if sublime:
	__OMEGALUL__.close()
if tofile and sublime:
	__LUL3D___.close()
# ----------------------------------------------