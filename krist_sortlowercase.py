"""
given a string. sort sort all lowercase letters in it lexicographically (a-z).
Ex
ASed12#azxd!! 
--> lower case positions AS__12#____!!
--> sort all lowercase -> aeddxz
--> output should be ASae12#ddxz!!
"""
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
from string import ascii_lowercase as lc
s = list(input().strip()) # list is mutable
for i  in range(len(s)):
	for j in range(i+1, len(s)):
		if s[i] > s[j] and s[i] in lc and s[j] in lc:
			s[i], s[j] = s[j], s[i]
print(''.join(s))

s = input().strip()
it = iter(sorted([x for x in s if x in lc])) 
out = [next(it) if char in lc else char for char in s]
print(''.join(out))


# ---------------- LOOOL 4HEad -----------------
if sublime:
	__OMEGALUL__.close()
if tofile and sublime:
	__LUL3D___.close()
# ----------------------------------------------
