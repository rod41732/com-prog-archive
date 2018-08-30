x1,x2,x3 = [input().strip() for i in range(3)]
x = x1+x2+x3
if len(x) != 9:
    print("ERROR")
else:
    win = '-'
    for i in range(3):
        if x[3*i] == x[3*i+1] == x[3*i+2]:
            win = x[3*i]
            break
        elif x[i] == x[i+3] == x[i+6]:
            win = x[i]
            break
    if win != '-':
        if x[0] == x[4] == x[8]:
            win = x[0]
        elif x[3] == x[4] == x[6]:
            win = x[3]
if win == '-':
    print('???')
else:
    print(win)