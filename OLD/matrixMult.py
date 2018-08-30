# def compare(a, b):
# # write your code here
# 	if a[1] < b[1]:
# 		return True
# 	elif a[1] == b[1] and a[0] > b[0]:
# 		return True
# 	return False


# n = int(input().strip())
# d = []
# for i in range(n):
# 	x, y = input().strip().split()
# 	d.append((x,float(y)))

# for kin range(n-1):
# 	for i in range(n-1):
# 		if compare(d[i], d[i+1]):
# 			d[i], d[i+1] = d[i+1], d[i]

# for i in d:print(i[0], i[1])


# m, n, p = [int(x) for x in input().split()]
# a = list()
# b = list()
# c = list()
# for i in range(m): # m rows
# 	x = input().strip().split()
# 	for num in x:
# 		a.append(int(num))

# for i in range(n): # n rows
# 	x = input().strip().split()
# 	for num in x:
# 		b.append(int(num))
# for i in range(m*p):
# 	_sum = 0
# 	x = [  a[j] for j in range(i//p*n, (i//p+1)*n)]
# 	y = [  b[j] for j in range(i%p, n*p, p) ]
# 	for j in range(n): # x, y has EXACTLY n elements
# 		_sum += x[j]*y[j]
# 	c.append(_sum)

# for i in range(m):
# 	S = ""
# 	for j in range(p):
# 		S += str(c[i*p+j]) + " "
# 	print(S.strip())
# 	


m, n, p = [int(x) for x in input().split()]
a = list()
b = list()
c = list()
for i in range(m): # m rows
	a.append([int(x) for x in input().strip().split()])
for i in range(n): # n rows
	b.append([int(x) for x in input().strip().split()])

for i in range(m):
	c.append([])
	for j in range(p):
		_sum = 0
		for k in range(n):
			_sum += a[i][k]*b[k][j]
		c[i].append(_sum)

for i in range(m):
	S = ""
	for j in range(p):
		S += str(c[i][j]) + " "
	print(S.strip())
	