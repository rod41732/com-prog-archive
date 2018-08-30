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
n, k = [int(e) for e in input().split()]
if k<=n:
	# s = '1'*k + '0'*(n-k)
	ans = []
	s = list(range(1, k+1))
	# t = '1'*k + '0'*(n-k)
	while s[0]+k <= n:
		ans.append(list(s))
		x = 1
		while s[-x:] == list(range(n+1-x,n+1)):
			x += 1
		x -= 1
		if x:
			s[-x-1] += 1
			s[-x:] = list(range(s[-x-1]+1, s[-x-1]+1+x)) 
		else:
			s[-1] += 1
		print(s)
	ans.append(list(s))
	# print(ans)
	for a in ans[::-1]:
		print(''.join(['1' if x in a else '0' for x in range(1, n+1)]))

# ---------------- LOOOL 4HEad -----------------
if sublime:
	__OMEGALUL__.close()
if tofile and sublime:
	__LUL3D___.close()
# ----------------------------------------------
