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
file = open('cards.txt', 'r')
n = int(input())
for i in range(n-1):
	file.readline()
cards = file.readline()
for i,c in enumerate(cards[1:]):
	prev = cards[i]
	curr = c
	prev = int(prev) if prev in '123456789' else 10 if prev=='0' else 1 if prev == 'A' \
		else 11 if prev == 'J' else 12 if prev == 'Q' else 13
	curr = int(curr) if curr in '123456789' else 10 if curr=='0' else 1 if curr == 'A' \
		else 11 if curr == 'J' else 12 if curr == 'Q' else 13
	if prev > curr:
		print('N')
		break
else:
	print('Y')
file.close()

# ---------------- LOOOL 4HEad -----------------
if sublime:
	__OMEGALUL__.close()
if tofile and sublime:
	__LUL3D___.close()
# ----------------------------------------------