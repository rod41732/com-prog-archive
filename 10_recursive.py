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
def solve_10_V1():
    print('chmcgqahkceg'[int(input())-1]) 
# solve_10_V1()

def solve_10_V2():
    def h(n):
        n = int(n)
        return 2*h(n-1)+1 if n>=1 else 0
    def gcd(x, y):
        x,y = int(x), int(y)
        return gcd(y, x%y) if y > 0 else x
    def J(n,k):
        n,k = int(n), int(k)
        return (J(n-1, k) + k)%n if n > 1 else 0
    def C(n):
        n = int(n)
        return sum(C(k)*C(n-1-k) for k in range(n)) if n>0 else 1
    def f(n):
        n = int(n)
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n%2 == 1:
            return f(n//2)**2 + f((n+1)//2)**2 
        else:
            return (2*f(n//2-1) + f(n//2))*f(n//2)
    def F(n):
        n = int(n)
        return 1 if n == 0 else n-M(F(n-1)) 
    def M(n):
        n = int(n)
        return 0 if n == 0 else n-F(M(n-1))

    def A(m,n):
        m, n = int(m), int(n)

        return A(m-1, 1) if m>0 and n==0 else\
        A(m-1, A(m, n-1)) if m>0 and n>0 else n+1

    exec(input().strip())
# solve_10_V2()

def solve_10_V3():
    import random
    def qsort( d ):
     if len(d) <= 1: return d
     p = d[random.randint(0,len(d)-1)] 
     return qsort([x for x in d if x < p])+[x for x in d if x == p]+qsort([x for x in d if x > p]) # เมื่อน า le ต่อกับ eq ต่อกับ mo ย่อมได้ข้อมูลเรียงล าดับจากน้อยไปมาก ก็คืนผลการต่อนี้กลับเป็นผลลัพธ์
    d = [int(e) for e in input().split()]
    d = qsort(d)
    print(' '.join([str(e) for e in d]))
# solve_10_V3()

def solve_10_V4():
    def sumlist(d):
      return d if type(d) is int else sum(sumlist(x) for x in d)

    print(sumlist(eval(input().strip())))
# solve_10_V4()

def solve_10_L1():
    # FUCKING HARD
    print(['ce', 'ab', 'h', 'j', 'dhjmn'][int(input())-1].upper())
# solve_10_L1()

def solve_10_L2():
    def x(n):
        if n > 0:
            tmp = x(n-1)
            return 3*tmp*(1-tmp) 
        return 0.01

    def M(n):
        return M(n-1) + sum(M(i)*M(n-i-2) for i in range(0, n-1)) if n>=2 else 1 

    def D(m, n):
        return 1 if m*n == 0 else D(m-1, n) + D(m, n-1) + D(m-1, n-1)

    def S(n):
        return ((6*n-9)*S(n-1)-(n-3)*S(n-2))//n if n>=3 else 1

    def d(n):
        return n*d(n-1) + (-1)**n if n>=1 else 1

    exec(input().strip())
# solve_10_L2()

def solve_10_L3():
    def dh(n, src, dst, tmp):
        if n == 0: return
        dh(n-1, src, dst, tmp)
        print('%dW : %s -> %s'%(n, src, tmp))
        print('%dB : %s -> %s'%(n, src, tmp))
        dh(n-1, dst, src, tmp)
        print('%dB : %s -> %s'%(n, tmp, dst))
        print('%dW : %s -> %s'%(n, tmp, dst))
        dh(n-1, src, dst, tmp)

    def dhanoi(n, left, mid, right):
      dh(n, left, right, mid)

    exec(input().strip())
# solve_10_L3()

def solve_10_L4():
    def copylist(L):
        return L if type(L) is not list else [copylist(x) for x in L]
  
    exec(input().strip())
# solve_10_L4()


def solve_10_P1():
    def f(n):
        return 1 if n==0 else n*f(n-1)
      
    print(f(int(input())))
# solve_10_P1()

def solve_10_P2():
    def fibo(n):
        return n if n <= 1 else fibo(n-1) + fibo(n-2)
      
    print(fibo(int(input())))
# solve_10_P2()

def solve_10_P3():
    def c(n,k):
        return 1 if k==0 or k==n else\
        c(n-1,k)+c(n-1,k-1) if 0 < k < n else 0

    n, k = int(input()), int(input())  
    print(c(n,k))

# solve_10_P3()

def solve_10_P4():
    def pmod(a, k, n):
        if k==0:
            return 1%n
        elif k%2==0:
            return (pmod(a, k//2, n)**2)%n
        else:
            return (a*pmod(a, k//2, n)**2)%n

    print(pmod(*[int(x) for x in input().split()]))
# solve_10_P4()


def solve_10_P5():
    def string2list(s):
        return eval(s)

    def isinlist(L, x):
        return x==L if type(L) is not list else any(isinlist(p, x) for p in L)

    ls = string2list(input().strip())
    x = int(input().strip())
    print(['Not Found', 'Found'][isinlist(ls, x)])
# solve_10_P5()

def solve_10_P6():
    def ks(i, w, v, x):
        if i < 0:
            return 0
        elif x >= w[i]:
            return max(ks(i-1, w, v, x-w[i])+v[i], ks(i-1, w, v, x))
        else:
            return ks(i-1, w, v, x)

    w = [int(e) for e in input().split()]
    v = [int(e) for e in input().split()]
    x = int(input())
    print(ks(len(w)-1, w, v, x))

# solve_10_P6()

def solve_10_P7():
    def f(d, c, s, b, m):
        if s == len(d) - 1:
            return m+1
        elif b and d[s+1] >= d[s]:
            return f(d, c+1, s+1, True, max(c+1, m))
        elif b and d[s+1] and d[s+1] < d[s]:
            return f(d, 0, s+1, False,  m)
        elif not(b) and d[s+1] >= d[s]:
            return f(d, 1, s+1, True, m)
        else:
            return f(d, 0, s+1, False, m)

    d = [int(e) for e in input().split()]
    print(f(d,0,0,False,0))  
# solve_10_P7()

def solve_10_P8():
    def gcd(a, b):
        return b if a%b == 0 else gcd(b, a%b)

    print(gcd(*(int(x) for x in input().split())))
# solve_10_P8()

def solve_10_P9():
    def isSorted(L):
        if len(L)<=2:
            return True 
        if L[0]<=L[1]<=L[-1]:
            return  isSorted(L[1:])
        if L[0]>=L[1]>=L[-1]:
            return isSorted(L[1:])
        return False

    n = int(input())
    ls = [int(e) for e in input().split()]
    print(['false', 'true'][isSorted(ls)])
#solve_10_P9()

def solve_10_P10():
    def tile(n, lastGreen):
        if n==0:
            return 1
        elif lastGreen:
            return 2*tile(n-1, False)
        else:
            return 2*tile(n-1, False) + tile(n-1, True)

    n = int(input())
    print(2*tile(n-1, False)+tile(n-1, True))
# solve_10_P10()

def solve_10_P11():
    def same_row(i,j):
        return i//9 == j//9
    def same_col(i,j):
        return i%9 == j%9
    def same_block(i, j):
        return i//27 == j//27 and i%9//3 == j%9//3
    def related(i, j):
        return same_block(i, j) or same_col(i, j) or same_row(i, j)
    
    def show(board):
        for i in range(3): 
            print('+---+---+---+')  
            for j in range(3): 
                k = 9*(3*i+j)   
                print('|'+board   [k:k+3]+'|'+board[k+3:k+6]+'|'+board[k+6:k+9]+'|') 
        print('+---+---+---+')

    def solve(board):
        if '.' not in board:
            return board
        
        ind = board.find('.')
        possible_sol = set('123456789')-{board[x] for x in range(81) if related(x, ind)}
        for e in possible_sol:
            newboard = board[:ind] + e + board[ind+1:]
            sol = solve(newboard)
            if sol != '':
                return sol
        return ''

    sol = solve(input().strip())
    show(sol)
# solve_10_P11()

def solve_10_P12():
    def doublelist(L):
        if type(L) is list:
            return [doublelist(L[i//2]) for i in range(2*len(L))]
        else:
            return L
    print(doublelist(eval(input().strip()))) 
# solve_10_P12()

def solve_10_P13():
    def recur(s):

        if s.islower():
            return {s}
        if len(s) == 0: 
        #in case of all caps -> it's possible that s == ''
        # which cause error if we continue  
            return {''}
        for i, e in enumerate(s):
            if e.isupper():
                break

        return {s[:i]+res for res in recur(s[i+1:])} | \
                {s[:i+1]+res for res in recur(s[i+1:])}

    s = input().strip()
    # filter out empty string
    # sorted -> sort result
    # use set to give unique strings
    print(*filter(None, sorted(recur(s))), sep='\n')
# solve_10_P13()

def solve_10_P14():
    def safe_dict(d, x):
        return d[x] if x in d else [] 
        
    mark = {}
    adj = {}
    n, a, b = [int(e) for e in input().split()]
    mark[a] = 1
    for i in range(n):
        x, y = [int(e) for e in input().split()]
        if x in adj:
            adj[x].append(y)
        else:
            adj[x] = [y]

    for i in range(a, b):
        if i in mark:
            for nxt in safe_dict(adj, i):
                mark[nxt] = 1

    # O(|V| + |E|) EZ Clap
    print(['no', 'yes'][b in mark])

# solve_10_P14()

def solve_10_P15():
    def safe_dict(d, x):
        return d[x] if x in d else [] 
        
    mark = {}
    adj = {} #adj[x] = list of room that warp TO x (not from x)
    n, a, b = [e for e in input().split()]
    for i in range(int(n)):
        y, x = [e for e in input().split()]
        if x in adj:
            adj[x].append(y)
        else:
            adj[x] = [y]

    for k, v in adj.items():
        adj[k] = sorted(v)

    #actually solving w/o recursive is posiible, using DP
    def find_path(x):
        if x == a:
            return [[a]]
        return [prevAnswer + [x] for prevRoom in safe_dict(adj, x) \
        for prevAnswer in find_path(prevRoom)]

    # need to fitler out duplicate path
    ans = sorted(set(' -> '.join(path) for path in find_path(b)))
    #
    print(*ans if ans else ['no'], sep='\n')

# solve_10_P15()

def solve_10_P16():
    def B2A(L):
        if L == []:
            return [[]]
        if type(L[0]) is int:
            return [[L[0]] + res for res in B2A(L[1:])]
        else:
            return [path for e in L for path in B2A(e)]

    print(B2A(eval(input().strip())))
# solve_10_P16()

def solve_10_P17():
    def flatten_dict(d):
        return {'': d} if type(d) is not dict else {(key+'.'+subkey).strip('.'):subval for key, val in d.items() for subkey, subval in flatten_dict(val).items()}


    d= flatten_dict(eval(input().strip()))
    # result = {key.strip('.'):val for key, val in flatten_dict(d).items()}
    for k in sorted(d.keys()): 
        print(k,':', d[k])

# solve_10_P17()


def solve_10_P18():
    # helper functions
    def up(board): 
        ind = board.index(0)
        if ind//4 == 0:
            return False
        else:
            board[ind], board[ind-4] = board[ind-4], board[ind]
            return True

    def down(board):
        ind = board.index(0)
        if ind//4 == 3:
            return False
        else:
            board[ind], board[ind+4] = board[ind+4], board[ind]
            return True

    def left(board):
        ind = board.index(0)
        if ind%4 == 0:
            return False
        else:
            board[ind-1], board[ind] = board[ind], board[ind-1]
        return True

    def right(board):
        ind = board.index(0)
        if ind%4 == 3:
            return False
        else:
            board[ind+1], board[ind] = board[ind], board[ind+1]
        return True
    # main DFS function
    def dfs(board, move, ans, maxdepth):
        if board == [*range(1, 16)] + [0]:
            print(ans)
            return True
        if move == maxdepth or board == '':
            return False

        if up(board):
            if dfs(board, move+1, ans+'U', maxdepth):
                return True
            down(board)

        if down(board):
            if dfs(board, move+1, ans+'D', maxdepth):
                return True
            up(board)

        if left(board):
            if dfs(board, move+1, ans+'L', maxdepth):
                return True
            right(board)

        if right(board):
            if dfs(board, move+1, ans+'R', maxdepth):
                return True
            left(board)
    
    found = False
    ls = [int(e) for e in input().split()]
    for max_depth in range(1,10):
        if dfs(ls, 0, "", max_depth):
            found = True
            break

    if not found:
        print("Cannot find answer")
# solve_10_P18()

# ---------------- LOOOL 4HEad -----------------
if sublime:
    __OMEGALUL__.close()
if tofile and sublime:
    __LUL3D___.close()
# ----------------------------------------------