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
        sys.stdout = __LUL3D___
def debug(*args):
        if debugging:
                print(*args)
# ----------------------------------------------

def solve_07_V1():
    print('dadbe'[int(input())-1])


def solve_07_V2():
    d = [int(x) for x in input().split()]
    mode = input().strip()
    print(sorted(d, reverse=(mode=='d')))


def solve_07_V3():
    file = open('hotels.txt', 'r')
    min_star = int(input().strip())
    to_tuple = lambda L: (L[0], int(L[1]), float(L[2]), ' '.join(L)) if int(L[1]) >= min_star else None
    hotels = list(filter(None, [to_tuple(line.strip().split(';')) for line in file]))
    file.close()

    if hotels:
      print(*(hotel[3] for hotel in sorted(hotels, reverse=True, key=lambda x:x[2])), sep='\n')
    else:
      print("Not Found")


def solve_07_V4():
    file = open('circulations.txt', 'r')
    today = input().strip()
    od = list(filter(lambda x: today > x[2], [line.split() for line in file]))
    print(*['Not Found'] if od == [] else (' '.join(book) for book in sorted(od, key=lambda x:x[2])), sep='\n')

def solve_07_L1():
    print(['j', 'k', 'g', 'tu', 'n'][int(input())-1])

def solve_07_L2():
    print(sorted([int(x) for x in input().split()]))

def solve_07_L3(): # TODO: continue from here
    ls = [int(x) for x in input().split()]
    n = len(ls)
    ls.sort()
    print((ls[(n-1)//2]+ls[n//2])/2)
        
def solve_07_L4():
    while True:
        cmd, a1, a2, a3, *rest = input().split() + ['']*3
        if cmd == 'Q':
            print("Bye!")
            break
        elif cmd == 'T':
            for item in data:
                if item[0] == a1:
                    item[2] += int(a2)
                    print(item)
                    break
            else:
                print('Product code does not exist.')
        elif cmd == 'U':
            for item in data:
                if item[0] == a1:
                    item[2] = int(a2)
                    print(item)
                    break
            else:
                print('Product code does not exist.')
        elif cmd == 'A':
            for item in data:
                if item[0] == a1:
                    print('Duplicate product code.')
                    break
            else:
                newitem = [a1, a2, int(a3)]
                data.append(newitem)
                print(newitem)
        elif cmd == 'D':
            for idx, item in enumerate(data):
                if item[0] == a1:
                    data[idx:idx+1] = []
                    print(a1, 'deleted')
                    break
            else:
                print('Product code does not exist.')

def solve_07_P1():
    s = input().strip()
    for char in '0123456789':
        print(s.count(char))

def solve_07_P2():
    s = input().strip()
    print(*[s.count(char) for char in '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'])

def solve_07_P3():
    file = open('.data.txt', 'r')
    ls = [[int(x) for x in line.split()] for line in file]
    file.close() 
    while True:
        x = int(input())
        if x == -1:
            break
        else:
            for std in ls:
                if std[0] == x:
                    print(std[1])
                    break
            else:
                print('Not Found')

def solve_07_P4():
    ls = []
    while True:
        x = int(input())
        if x == -1: 
            break
        else: 
            ls.append(x)
    ls.sort()
    n = len(ls)
    print(next((ls[x] for x in range(n-n//2) if ls[x] == ls[x+n//2]),'Not found'))

def solve_07_P5():
    n = int(input())
    print(*sorted([int(input()) for i in range(n)], reverse=True), sep='\n')

def solve_07_P6():
    n = int(input())
    a = [int(input()) for i in range(n)]
    mean = sum(a)/n
    a.sort()
    med = (a[n//2]+a[(n-1)//2])/2
    mod = max((a.count(num), num) for num in a)[1]
    print(mean, med, mod)

def solve_07_P7():
    print(*sorted([int(line.split()[0]) for line in open('score.txt')]), sep='\n')

def solve_07_P8():
    print(*sorted([int(line.split()[0]) for line in open('score.txt')], reverse=True), sep='\n')

def solve_07_pP9():
    print(*sorted([int(x) for x in input().split()], key=lambda x:[x%2, -x if x%2 else x]))

def solve_07_P10():
    n = int(input())
    ls = [input().strip() for i in range(n)]
    should_swap = lambda x,y: len(x)>len(y) or len(x) == len(y) and x>y
    cnt = 0
    for k in range(n-1):
        for i in range(n-1):
            if should_swap(ls[i], ls[i+1]):
                ls[i], ls[i+1] = ls[i+1], ls[i]
                cnt += 1
    print('\n'.join(ls), cnt, sep='\n')


def solve_07_P11():
    gl = 'F D D+C C+B B+A'
    gn = [0, 1, 1.5, 2, 2.5, 3, 3.5, 4]
    r, c = [int(x) for x in input().split()]
    for i in range(r):
        cnt = _sum = 0
        for g in input().split():
            if g in gl:
                cnt += 1
                _sum += gn[gl.find(g)//2]
        print("%.2f"%(_sum/cnt))


def solve_07_P12():
    x, n = [int(e) for e in input().split()]
    ans = 0
    comp = (lambda a,b: a>=b) if x == 0 else (lambda a,b: a<=b)
    a = [[int(x) for x in input().split()] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if comp(i,j):
                ans += a[i][j]
    print(ans)

def solve_07_P13():
        r,c = int(input()), int(input())
        a = [input().strip() for i in range(r)]
        for i in range(r):
            for j in range(i+1, r):
                if a[i] == a[j]:
                    print(i+1, a[i], j+1, a[j], sep='\n')
#---------------------------------------------------#---------------------------------------------------
def solve_07_P14():
        r, c = [int(e) for e in input().split()]
        a = [[int(e) for e in input().split()] for i in range(r)]
        mr, mc = [], []
        for i in range(r):
            mn = a[i][0]
            for j in range(c):
                if a[i][j] < mn:
                    mn = a[i][j]
            mr.append(mn)
        for i in range(c):
            mx = a[0][i]
            for j in range(r):
                if a[j][i] > mx:
                    mx = a[j][i]
            mc.append(mx)
        found = False
        for i in range(r):
            if found: break
            for j in range(c):
                if a[i][j] == mr[i] == mc[j]:
                    print(a[i][j])
                    found = True
                    break
        if not found:
            print(-1)

#---------------------------------------------------#---------------------------------------------------
def solve_07_P15():
        n = int(input())
        a = [[int(e) for e in input().split()] for i in range(n)]
        for i in range(n):
            sCol = 0
            sRow = 0
            for j in range(n):
                sCol += a[j][i]
                sRow += a[i][j]
            if sRow == 1 and sCol == n:
                print(i)
                break
        else:
            print(-1)
#---------------------------------------------------#---------------------------------------------------
def solve_07_P16():
        r,c = [int(e) for e in input().split()]
        a = [[0]*c for i in range(r)]
        for k in range(2):
            for i in range(r):
                t = [int(x) for x in input().split()] #input row
                for j in range(c):
                    a[i][j] += t[j]
        for i in range(r):
            print(*a[i])
#---------------------------------------------------#---------------------------------------------------
def solve_07_P17():
        std = []
        while True:
            inp = [float(e) for e in input().split()]
            if len(inp) == 2:
                std.append(inp)
            else:
                std.sort(key=lambda x: (-x[1], x[0]))
                for i in range(len(std)):
                    if std[i][0] == inp[0]:
                        print(i+1)
                        break
                else:
                    print('Not Found')
                break
#---------------------------------------------------#---------------------------------------------------
def solve_07_P18():
        n = int(input())
        a = []
        for i in range(n):
            x = input().strip()
            a.append([*[x.count(char) for char in 'abcdefghijklmnopqrstuvwxyz'], x])
        a.sort()
        for c in a:
            print(c[-1])
# ---------------- LOOOL 4HEad -----------------
if sublime:
        __OMEGALUL__.close()
if tofile and sublime:
        __LUL3D___.close()
# ----------------------------------------------