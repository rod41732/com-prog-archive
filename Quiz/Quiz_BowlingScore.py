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
data, index = input().strip(), int(input())
number = []
framescore = [0]*10
for i, c in enumerate(data):
	if c in '0123456789':
		number.append(int(c))
	elif c == 'X':
		number.append(10)
	else:
		number.append(10-number[-1]) # 10-last

frmId = cnt = 0
for i, c in enumerate(data) :
	if frmId == 9:
		framescore[9] += number[i]
	elif c in '1234567890':
		framescore[frmId] += number[i]
		cnt += 1
		if cnt == 2:
			cnt = 0
			frmId += 1
	elif c == '/':
		framescore[frmId] += number[i] + number[i+1]
		cnt = 0
		frmId += 1
	elif c == 'X':
		framescore[frmId] += number[i] + number[i+1] + number[i+2]
		cnt = 0
		frmId += 1
if 1 <= index <= 10:
	print(framescore[index-1])
else:
	print(sum(framescore))
# ---------------- LOOOL 4HEad -----------------
if sublime:
	__OMEGALUL__.close()
if tofile and sublime:
	__LUL3D___.close()
# ----------------------------------------------
