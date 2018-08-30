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
t = int(input())
cnt = 0
for xx in range(t):
	num = int(input())
	sum_divisor = sum(x for x in range(1,num//2+1) if num%x == 0)
	if sum_divisor == num:
		print('%d is perfect'%(num,))
		print(','.join(str(x) for x in range(1,num//2+1) if num%x == 0) + ',')
		cnt+=1
	else:
		print('%d is not perfect'%(num,))
print(cnt)
# ---------------- LOOOL 4HEad -----------------
if sublime:
	__OMEGALUL__.close()
if tofile and sublime:
	__LUL3D___.close()
# ----------------------------------------------