n = int(input())
sum = 0
for i in range(1, n+1):
    for j in range(1, i+1):
        for k in range(j, i+1):
            sum += (-1)**i*j*k
print(sum)