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
a, b, c = [float(x) for x in input().strip().split()]
if a == 0:
	if b!= 0:
		print('{:.2f}'.format(-c/b))
	elif b == 0:
		if c == 0:
			print('Roots are any numbers')
		else:
			print('No roots exists')
else:
	if a < 0:
		# if a < 0 -b-dis/2a will be greater than -b+dis/2a
		# so we need to make a > 0
		a, b, c = -a, -b, -c 
	disc = b**2-4*a*c
	if disc == 0: # 1 root
		print("{:.2f}".format(-b/(2*a)))
	elif disc < 0:
		print('Roots are complex numbers')
	elif disc >= 0:
		print('{:.2f} {:.2f}'.format((-b-disc**0.5)/(2*a), (-b+disc**0.5)/(2*a)))

# ---------------- LOOOL 4HEad -----------------
if sublime:
	__OMEGALUL__.close()
if tofile and sublime:
	__LUL3D___.close()
# ----------------------------------------------