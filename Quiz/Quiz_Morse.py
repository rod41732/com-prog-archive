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
file = open(input().strip(), 'r')
mode, pattern = file.readline().strip(), file.readline().strip()
if mode not in ['M2T', 'T2M']:
	print('Invalid code')
else:
	convert = []
	pattern = pattern[1:]
	while True:
		ind = pattern.find(']')
		if not pattern:
			break
		convert.append([pattern[:ind]])
		convert[-1].append(pattern[ind+1:ind+2])
		pattern = pattern[ind+3:]
	if mode == 'M2T':
		for line in file:
			ans = ''
			for morse in line.strip().split():
				for x in convert:
					if x[0] == morse: #found
						ans += x[1]
						break
				else:# not found, which break main loop
					print('Invalid :', line.strip())
					break
			else: #not break = no error
				print(ans)
	else:
		for line in file:
			ans = []
			for char in line.strip():
				for x in convert:
					if x[1] == char: #found
						ans.append(x[0])
						break
				else:# not found, which break main loop
					print('Invalid :', line.strip())
					break
			else: #not break = no error
				print(*ans)





	# for i in range(len(sfrom)):
	# 	print(sfrom[i], '->', sto[i])
# ---------------- LOOOL 4HEad -----------------
if sublime:
	__OMEGALUL__.close()
if tofile and sublime:
	__LUL3D___.close()
# ----------------------------------------------