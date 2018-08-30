d, m, y = [int(x) for x in input().strip().split()]
days = ['SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI']
if m < 3:
    m += 12
    y -= 1
c = y//100
k = y%100
w = (d + (26*(m+1))//10 + k + k//4 + c//4 + 5*c)%7
print(days[w]) # TOO FUCKING LAZY TO WRITE 7 IFs
