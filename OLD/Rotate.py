op, row = input(), int(input())
inp = []
for i in range(row):
    inp.append(input().strip())
col = len(inp[0])

for i in range(row):
    if len(inp[i]) != len(inp[0]):
        print("Invalid size")
        break
else:
    if op == '90':
        out = ['']*col
        for i in range(col):
            for j in range(row):
                out[i] += inp[row-1-j][i]
        for i in range(col):
            print(out[i])
    elif op == 'flip':
        for i in range(row):
            print(inp[i][::-1])
    else:
        for i in range(row):
            print(inp[row-1-i][::-1])