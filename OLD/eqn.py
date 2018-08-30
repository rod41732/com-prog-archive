n = int(input())
mat = []
for i in range(n):
	mat.append([float(x) for x in input("EQ%d:" % (i,)).split()])

for i in range(n):
	if (mat[i][i] == 0.0):  # swap eq
		for j in range(i + 1, n):
			if (mat[j][i] != 0.0):
				mat[i], mat[j] = mat[j], mat[i]
		else:
			print("Error")
	for j in range(i + 1, n):
		for k in range(n + 1):
			mat[j][k] -= mat[i][k] * mat[j][i] / mat[i][i]

for i in range(n):
	x = mat[i][i]
	for j in range(i, n+1):
		mat[i][j] /= x



for i in range(n):
	print(mat[i])


for i in range(n - 1, -1, -1):
	if (mat[i][i] == 0):
		print("Error")
	for j in range(i - 1, -1, -1):
		for k in range(n+1):
			mat[j][k] -= mat[i][k] * mat[j][i] / mat[i][i]
for i in range(n):
	mat[i][n] /= mat[i][i]
	mat[i][i] = 1

for i in range(n):
	print(mat[i])




