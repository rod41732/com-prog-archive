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
s = input().strip()
out = ''
char_set = ['0123456789', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz']
while s:
	offset = int(s[0])
	num = int(s[1])
	s = s[2:] #skip num, offset so first N characters in to be decoded
	for char in s[:num]:
		for cs in char_set:
			if char in cs:
				ind = cs.index(char)
				out += cs[(ind+offset)%len(cs)]
				break
		else:
			out += char
	s = s[num:] #remove decoded chars
print(out)



# ---------------- LOOOL 4HEad -----------------
if sublime:
	__OMEGALUL__.close()
if tofile and sublime:
	__LUL3D___.close()
# ----------------------------------------------