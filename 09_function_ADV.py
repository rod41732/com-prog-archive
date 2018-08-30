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

def solve_09_V1():
    print('adjapegeeb'[int(input())-1])


def solve_09_V2():
    from itertools import cycle

    def fac(n):
        return '{}!'.format(n)
    
    def oneterm(x, n):
        return '{}**{}/{}!'.format(x,n,n)

    def sin(x, n):
        out = str(x)
        it = cycle('-+')
        for i in range(3, 2*n, 2):
            out += ' {} {}'.format(next(it), oneterm(x, i))
        return out.strip()
    
    exec(input().strip())

def solve_09_V3():
    def read_date():
        mname = {"Jan":1,"Feb":2,"Mar":3,"Apr":4,
        "May":5,"Jun":6,"Jul":7,"Aug":8,
        "Sep":9,"Oct":10,"Nov":11,"Dec":12}
        date = input().split() 
        d = int(date[0]) 
        m = mname[date[1][:3]] 
        y = int(date[2]) 
        return (d, m, y)

    def zodiac(day, month):
        if  day >= 22 and month==3  or day <=21 and month==4 :
            return "Aries" 
        elif day >= 22 and month==4  or day <=21 and month==5 :
            return "Taurus" 
        elif day >= 22 and month==5  or day <=21 and month==6  :
            return "Gemini" 
        elif day >= 22 and month==6  or day <=21 and month==7  :
            return "Cancer" 
        elif day >= 22 and month==7  or day <=21 and month==8  :
            return "Leo" 
        elif day >= 22 and month==8  or day <=21 and month==9  :
            return "Virgo" 
        elif day >= 22 and month==9  or day <=21 and month==10 :
            return "Libra" 
        elif day >= 22 and month==10 or day <=21 and month==11 :
            return "Scorpio" 
        elif day >= 22 and month==11 or day <=21 and month==12 :
            return "Sagittarius" 
        elif day >= 22 and month==12 or day <=20 and month==1  :
            return "Capricorn" 
        elif day >= 21 and month==1  or day <=20 and month==2  :
            return "Aquarius" 
        elif day >= 21 and month==2  or day <=21 and month==3  :
            return "Pisces"

    def days_in_feb(y):
        return 29 if (y % 400 == 0 or y% 100 != 0 and y%4 == 0) else 28

    def days_in_month(m,y):
        return 30 if m in (4, 6, 9, 11) \
        else days_in_feb(y) if m == 2 else 31

    def days_in_between(d1,m1,y1,d2,m2,y2):
        ans = 0
        ans += sum(days_in_month(i, y1) for i in range(12, 1, -1) if m1 < i)
        ans += sum(days_in_month(i, y2) for i in range(1, 12) if m2 > i)
        ans += (days_in_month(m1, y1) - d1 + 1) + int((y2 - y1 - 1)*365.25)+ (d2 - 1)
        return ans

    def main():
        d1,m1,y1 = read_date()
        d2,m2,y2 = read_date()
        print(zodiac(d1, m1), zodiac(d2, m2))
        print(days_in_between(d1, m1, y1, d2, m2, y2))

    exec(input().strip())

def solve_09_V4():
    def make_int_list(x):
        return [int(e) for e in x.split()]

    def is_odd(x):
        return x%2 == 1

    def odd_list(ls):
        return [x for x in ls if x%2 == 1]

    def sum_square(ls):
        return sum(x*x for x in ls)

    exec(input().strip())

def solve_09_L1():
    print('daaea'[int(input())-1])

def solve_09_L2():
    def knows(R, x, y):
        return y in R[x]

    def is_celeb(R, celeb):
        return True if all(knows(R, person, celeb) for person in R.keys() if person != celeb) and \
            all(not knows(R, celeb, person) for person in R.keys() if person != celeb) else False

    def find_celeb(R):
        for person in R:
            if is_celeb(R, person):
                return person
        return None

    def read_relations():
        R = dict()
        while True:
            p1, p2, *_ = input().split() + ['']
            if p2 == '': break
            else:
                if p1 in R:   R[p1].add(p2)
                else:   R[p1] = {p2}
                if p2 not in R:   R[p2] = set()
        return R
    def main():
        R = read_relations()
        c = find_celeb(R)
        print(c if c else 'Not Found')

    exec(input().strip())

def solve_09_L3():

    def extract_sign(t):
        sign = ''
        if t[0] == '-':
            t = t[1:]
            sign = 'lop-'
        return sign, t

    def split_by_point(t):     
        ind = t.find('.')
        after = ''
        if ind != -1:
            after = t[ind+1:]
            t = t[:ind] # before
        return t, after

    def remove_comma(t):
        return t.replace(',', '')

    def split_by_million(t):
        million = ''
        if len(t) > 6:
            million = t[:-6]
            t = t[6:]
        return million, t

    def digit_to_text(dgt):
        digits = 'soon nuengsong sam  see  ha   hok  jed  pad  kao  '
        return digits[dgt*5:dgt*5+5].strip()

    def pos_to_text(p):
        p = int(p)
        pos = '    sip roeypun muensaenlarn'
        return pos[p*4:p*4+4].strip()

    def right_of_jood_to_text(t):
        out = ''
        for d in t:
            out += '-' + digit_to_text(int(d))
        return out

    def fix(t): 
        t = t.replace('song-sip', 'yee-sip')
        t = t.replace('-soon', '')
        t = t.replace('nueng-sip', 'sip')
        t = t.replace('sip-nueng', 'sip-ed')
        return t

    def number_to_text(number):
        out = ''
        n = len(number)
        for i, digit in enumerate(number):
            if digit == '0':
                out += digit_to_text(int(digit)) + '-'
            else:
                out += digit_to_text(int(digit)) + '-' + pos_to_text(n-i-1) + '-'
        return fix(out.strip('-'))


    def combine(moreM, lessM):
        if moreM == '' and lessM == '':
            return 'soon'
        elif moreM == '' and lessM != '':
            return lessM
        elif moreM != '' and lessM == '':
            return moreM + '-larn'
        else:
            return moreM + '-larn-' + lessM


    def main():
        num          = remove_comma(input().strip())
        sign,num     = extract_sign(num)
        leftJ,rightJ = split_by_point(num)
        moreM,lessM  = split_by_million(leftJ)
        tLessM       = number_to_text(lessM)
        tMoreM       = number_to_text(moreM)
        out= combine(tMoreM, tLessM)

        if rightJ != '' :
            out += '-jood' + right_of_jood_to_text(rightJ)

        print((sign + out).strip('-'))

    exec(input().strip())

def solve_09_L4():
    def row_number(t, e):
        return next(i for i in range(len(t)) if e in t[i])

    def flatten(t):
        return [x for sublist in t for x in sublist if x!=0]

    def inversions(t):
        return sum(1 for i in range(len(t)) for j in range(i+1, len(t)) if t[i]>t[j])

    def solvable(t):
        n = len(t)
        zero_pos = row_number(t, 0)
        inv = inversions(flatten(t))
        return True if (n%2 == 1 and inv%2 == 0 or 
        n%2 == 0 and inv%2 != zero_pos%2 ) else False

    exec(input().strip())

def solve_09_P1():
    def function1():
        sum = 0
        for i in range(10):
            sum += i
        return sum

    def function2(n):
        i = 2
        n = int(n)
        if n == 1:
            return False
        while i <= n**0.5:
            if n%i == 0:
                return False
            i += 1
        return True

    def function3(n):
        n = int(n)
        for i in range(1,n):
            if function2(i):
                print(i)

    def function4(x,y):
        match = 0
        notmatch = ''
        for i in x:
            if i == y:
                match += 1
            else:
                notmatch += i
        return [match,notmatch]

    x = input().strip()
    y = input().split() if x != 'function1' else []
    ret = eval(x)(*y)
    if ret is not None:
        print(ret)

def solve_09_P2():
    from math import ceil, floor
    def nextEven(f):
        x = int(ceil(f))
        x += 1 if x%2 != 0 else 0
        return x

    def nextOdd(f):
        x = int(ceil(f))
        x += 1 if x%2 == 0 else 0
        return x

    while True:
        x = float(input())
        if x < 0:
            break
        even = nextEven(x)
        odd = nextOdd(x)
        print((even, odd))

def solve_09_P3():
    def compare(a, b):
        return (-a[1], a[0]) > (-b[1], b[0])

    n = int(input().strip())
    d = []
    for i in range(n):
        x, y = input().strip().split()
        d.append((x,float(y)))

    for k in range(n-1):
        for i in range(n-1):
            if compare(d[i], d[i+1]):
                d[i], d[i+1] = d[i+1], d[i]

    for i in d:
        print(i[0], i[1])

def solve_09_P4():
    def det3(m):
        a = m[0][0]*m[1][1]*m[2][2]
        b = m[0][1]*m[1][2]*m[2][0]
        c = m[0][2]*m[1][0]*m[2][1]
        d = m[0][2]*m[1][1]*m[2][0]
        e = m[0][0]*m[1][2]*m[2][1]
        f = m[0][1]*m[1][0]*m[2][2]
        return a+b+c-d-e-f

    def minor(m, row, col):
        return [[m[i][j] for j in range(len(m)) if j!= col] \
         for i in range(len(m)) if i != row] 


    def det4(m):
        return sum((-1)**i*det3(minor(m, 0, i))*m[0][i] for i in range(4))

    matrix = [[int(e)for e in input().split()] for i in range(4)] 
    print(det4(matrix))   

def solve_09_P5():
    def substr2num(s):
        pair=dict([['CM',900],['CD',400],['XC',90],['XL',40],['IX',9],['IV',4]])
        single=dict([['M',1000],['D',500],['C',100],['L',50],['X',10],['V',5],['I',1]])
        return (pair[s], 2) if s in pair.keys() else (single[s[:1]], 1)
    
    def roman2num(s):
        ans = 0
        while s:
            x, y = substr2num(s[:2])
            ans += x
            s = s[y:]
        return ans

    n = int(input())
    ls = [input().strip() for i in range(n)]
    print(*sorted(ls, key=roman2num), sep='\n')

def solve_09_P6():
    def read_data():
        docs = {}
        n = int(input().strip())
        for i in range(n):
            tokens = input().strip().split()
            doc_name = tokens[0]
            doc_keywords = tokens[1:]
            for kword in doc_keywords:
                if kword in docs.keys():
                    docs[kword].add(doc_name)
                else:
                    docs[kword] = {doc_name}
        return docs
    
    def safe_dict(d, key):
        return d[key] if key in d else set()

    def search(docs, condition, search_keywords):
        first, *rest = search_keywords
        if condition not in ('and', 'or'):
            return []
        ans = safe_dict(docs, first)
        if condition == 'and':
            for kw in rest:
                ans = ans & safe_dict(docs, kw)
        if condition == 'or':
            for kw in rest:
                ans = ans | safe_dict(docs, kw)
        return ans

    docs = read_data()
    tokens = input().split()
    print( sorted( search(docs, tokens[0], tokens[1:]) ))

def solve_09_P7():
    def f(x):
        k = 0
        for i in range(1,2*x,2):
            k += i
        for j in range(k):
            if j%x==0:
                k+=2
        return k+3
    def f_inv(x):
        return int((x-2)**0.5-1)

    print(eval(input().strip()))

def solve_09_P8():
    def isSet(c1, c2, c3):
        return not any(len(set(component)) == 2 for component in zip(c1, c2, c3))
    cards= []
    for i in range(12):
        cards.append(input().strip().split())

    for i in range(12):
        for j in range(i+1,12):
            for k in range(j+1,12):
                if isSet(cards[i],cards[j],cards[k]):
                    print(i,j,k)

def solve_09_P9():
    def isSevenUp(x):
        return x%7 == 0 or '7' in str(x)
    def nextSevenUp(x):
        return next(i for i in range(x+1, x+8) if isSevenUp(i))

    def prevSevenUp(x):
        return next(i for i in range(x-1, x-8, -1) if isSevenUp(i))

    f,x = input().strip().split()
    x = int(x)
    if   f == 'isSevenUp': print(isSevenUp(x))
    elif f == 'nextSevenUp': print(nextSevenUp(x))
    elif f == 'prevSevenUp': print(prevSevenUp(x))


def solve_09_P10():
    def distance(p,q):
        return ( (p[0]-q[0])**2 + (p[1]-q[1])**2 )**0.5
    def perimeter(points):
        return sum(distance(points[i-1], points[i]) for i in range(len(points)))
    s = input().strip().split()
    p = [(float(t[1:t.find(',')]),float(t[t.find(',')+1:-1]))for t in s]
    print(perimeter(p))

def solve_09_P11():
    def zscore(L):
        mean = sum(L)/len(L)
        sd = (sum(x**2 for x in L)/len(L) - mean**2)**0.5
        return [(x-mean)/sd for x in L]
    L = [float(e)for e in input().split()]
    for i in zscore(L):
        print(i)

def solve_09_P12():
    def eat(q1, q2):
        dx, dy = q1[0]-q2[0], q1[1]-q2[1]
        return True if dx == 0 or dy == 0 or abs(dx) == abs(dy) else False

    def all_eat(L):
        return [(i, j) for i in range(len(L)) for j in range(i+1, len(L)) if eat(L[i], L[j])]

    print(eval(input().strip()))

def solve_09_P13(): #literally 09_L4 OMEGALUL
    def row_number(t, e):
        return next(i for i in range(len(t)) if e in t[i])

    def flatten(t):
        return [x for sublist in t for x in sublist if x!=0]

    def inversions(t):
        return sum(1 for i in range(len(t)) for j in range(i+1, len(t)) if t[i]>t[j])

    def solvable(t):
        n = len(t)
        zero_pos = row_number(t, 0)
        inv = inversions(flatten(t))
        return True if (n%2 == 1 and inv%2 == 0 or 
        n%2 == 0 and inv%2 != zero_pos%2 ) else False

    exec(input().strip())

solve_09_P13()
        

# ---------------- LOOOL 4HEad -----------------
if sublime:
    __OMEGALUL__.close()
if tofile and sublime:
    __LUL3D___.close()


# ----------------------------------------------
