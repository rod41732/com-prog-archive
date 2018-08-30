# conditional 
def solve_02_V1():
    print('ebebb'[int(input())-1])

def solve_02_V2():
    print(*sorted([int(input()) for i in range(4)]))

def solve_02_V3():
    ls = [float(input()) for i in range(6)]
    print(min(ls), max(ls))

def solve_02_V4():
    d, m, y = [int(input()) for i in range(3)]
    y -= 543
    dim = [0, 31, 29 if y%4==0 and y%100!=0 or y%400 == 0 else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    print(sum(dim[i] for i in range(m)) + d)

def  solve_02_L1():
    print([ 'a', 'v', 'n', 'p', 'efghijklmv' ][int(input())-1].lower())

def  solve_02_L2():
    print(sorted([int(input()) for i in range(5)])[2])

def solve_02_L3():
    n = int(input())
    if n < 0 or n > 80:
      print("Error : Out of range")
    else:
      print(''.join([str(n//3**i%3) for i in range(3, -1, -1)]))

def solve_02_L4():  #--> By github.com/krist7599555
    import math

    def ems(weight):
    	limits = [32, 37, 42, 52, 67, 82, 97, 122, 137, 157, 177, 197, 217, 242, 267, 292, 317, 342, 367, 397, 427, 457, 487];
    	costs = [20, 100, 250, 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500, 10000]
    	return next((cost for limit, cost in zip(costs, limits) if weight <= limit), 'ERROR')
    	# next(iter) returns first 'entry' in iter if first used/ deafult when exhausted
    def rgs(weight):
    	limits = [18, 22, 28, 38, 58];
    	costs = [100, 250, 500, 1000, 2000]
    	return next((cost for limit, cost in zip(costs, limits) if weight <= limit), 'ERROR')
      
    def nrm(weight):
    	return 5 + 15 * math.ceil(weight / 1e3)

    cm = input().strip()
    weight = int(input())
    print({'N':nrm, 'E':ems, 'R':rgs}[cm](weight) if weight > 0 else 'ERROR')

def solve_02_P1():
    n = int(input().strip())
    sign = 'positive' if n > 0 else 'negative' if n < 0 else 'zero'
    parity = 'odd' if n%2 == 1 else 'even'
    print(sign, parity, sep='\n')

def solve_02_P2(): # idea -> krist7599555
    lms = [0, 50, 55, 60, 65, 70, 75, 80, 101]
    grd = ['ERROR', 'F', 'D', 'D+', 'C', 'C+', 'B', 'B+', 'A']
    score = float(input())
    print(next((gd for lm, gd in zip(lms, grd) if score < lm), 'ERROR'))

def solve_02_P3():
    a, b, c = sorted([int(x) for x in input().strip().split()])
    print('NO' if a+b <= c else 'YES')

def solve_02_P4():
    lms = [15, 60, 120, 180, 240, 300, 360]
    cst = [0, 10, 20, 30, 50, 70, 90]
    h1, m1, h2, m2 = [int(input()) for i in range(4)]
    dt = 60*(h2-h1) + m2-m1
    print(next((cost for cost, limit in zip(cst, lms) if dt <= limit), 200))

def solve_02_P5():
    pr, cou, card = (input().strip() for i in range(3))
    print(float(pr)*(100- [0,10,5,20][1*(card == 'Y') + 2*(cou == "Y")])/100)

def solve_02_P6():
    a1, b1, c1 = [int(x) for x in input().strip().split()]
    a2, b2, c2 = [int(x) for x in input().strip().split()]
    if a1*b2 != a2*b1:
      print('one solution')
    elif b1*c2 != b2*c1 or a1*c2 != a2*c1:
      print('no solution')
    else:
      print('many solutions')

def solve_02_P7():
    inc = int(input())
    amt = [100000, 400000, 500000, 3000000, inc]
    rate = [.05, .1, .2, .3, .37]
    print(sum(max(min(a, inc-sum(amt[:i])), 0)*r for i, a, r in zip(range(5), amt, rate)))


def solve_02_P8():
    n = int(input().strip())-543
    print(29 if n%4 == 0 and n%100 != 0 or n%400 == 0 else 28)

def solve_02_P9():
    m, y = [int(x) for x in input().strip().split()]
    y -= 543
    days = [0, 31, 29 if (y%4 == 0 and y%100 != 0) or y%400 == 0 else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    print(days[m])

def solve_02_P10():
    d, m, y = [int(x) for x in input().strip().split()]
    if m < 3:
        m += 12
        y -= 1
    c = y//100
    k = y%100
    w = (d + (26*(m+1))//10 + k + k//4 + c//4 + 5*c)%7
    print(['SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI'][w])

def solve_02_P11():
    x1, y1, r1, x2, y2, r2 = [float(x) for x in input().strip().split()]
    diff = ((x1-x2)**2 + (y1-y2)**2)**0.5 - (r1+r2)
    print(1 if diff == 0 else 2 if diff < 0 else 3)

def solve_02_P12():
    amax, a = [int(x) for x in input().strip().split()]
    bmax, b = [int(x) for x in input().strip().split()]
    b += a; a = 0
    if b > bmax:
        a = b-bmax
        b = bmax
    print(a, b)
