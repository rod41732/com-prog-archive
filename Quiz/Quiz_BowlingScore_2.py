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
def score(ind):
	c = x[ind%len(x)] #return garbage when notit range 
	return int(c) if c.isdigit() else 10 if c=='X' else 10-score(x[ind-1])

def index(it, char):
	x = next(it, 11)
	return x if char != 'X' else next(it, 11)

frame_counter = iter([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10])
x, n = input().strip(), int(input())
func = (lambda x: x==n) if 1<=n<=10 else (lambda x: 1<=x<=10)
print(sum( score(i) + (score(i+1) if char in '/X' else 0) + (score(i+2) if char == 'X' else 0) \
	for i,char in enumerate(x) if func(index(frame_counter, char)) ))
# ---------------- LOOOL 4HEad -----------------
if sublime:
	__OMEGALUL__.close()
if tofile and sublime:
	__LUL3D___.close()
# ----------------------------------------------