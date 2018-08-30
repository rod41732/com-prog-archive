#V1 __________________________________________
print('cdcdd'[int(input())-1])

#V2 __________________________________________
import math
class Circle:
    def __init__(self,index,x,y,r):
        self.index = index
        self.x = x
        self.y = y
        self.r = r
    def touch(self,other):
        d = distance(self.x, self.y, other.x, other.y)
        if d < self.r + other.r:
            return 'Overlap'
        elif abs(d-self.r + other.r)  <= 1e-5:
            return 'Touch'
        return 'Free'
def distance(x1,y1,x2,y2): # หาระยะห่างระหว่างจุดสองจุด
    return ((x1-x2)**2+(y1-y2)**2)**0.5
    

# ส่วนของโปรแกรมหลัก
n = int(input().strip())
circles = []
for i in range(n):
    circle_input = [int(e) for e in input().strip().split()]
    circle = Circle(*circle_input)
    circles.append(circle)
output = []
# วน loop เช็ควงกลมทุกวง ส่วนนี้ให้เขียนเอง ถ้าเจอวงกลมที่ Free ให้เอามาเก็บใน output
for c in circles:
    if all(c.touch(other) == 'Free' for other in circles if other.index != c.index):
        output.append(c.index)
if len(output) == 0:
    print('Not Found')
else:
    print(' '.join([str(e) for e in output]))



#V3 __________________________________________
import math
class Circle:
    def __init__(self,index,x,y,r):
        self.index = index
        self.x = x
        self.y = y
        self.r = r
    def line_intersection(self,line):
    # หาจุดตัดของ “เส้นตรง” และวงกลม ค่าที่ return เป็ น tuple ของจ านวนจุดตัด ตามด้วยพิกัดของจุดตัดที่เป็ นค าตอบ
        if line.x1 != line.x2:
            # line: y = Mx+B
            M = (line.y2-line.y1)/(line.x2-line.x1)
            B = line.y1-M*line.x1
            # แก้สมการจาก (x-self.x)**2+(y-self.y)**2 = self.r**2
            a = M**2+1
            b = -2*self.x + 2*M*(B-self.y)
            c = self.x**2+(B-self.y)**2-self.r**2
            if b**2 > 4*a*c:
                ans1 = (-b + math.sqrt(b**2-4*a*c))/2/a
                ans2 = (-b - math.sqrt(b**2-4*a*c))/2/a
                return (2,(ans1,M*ans1+B),(ans2,M*ans2+B))
            elif b**2 == 4*a*c:
                return (1,(-b/2/a,M*(-b/2/a)+B))
            else:
                return (0,)
        else:
            if self.r**2 == (line.x1-self.x)**2:
                return (1,(line.x1,self.y))
            elif self.r**2 > (line.x1-self.x)**2:
                rr = math.sqrt(self.r**2 - (line.x1-self.x)**2)
                ans1 = rr+self.y
                ans2 = rr-self.y
                return (2,(line.x1,ans1),(line.x2,ans2))
            else:
                return (0,)
    def contain_point(self,px,py):
    # ทดสอบว่าจุดอยู่ในวงกลมหรือไม่ ถ้าอยู่จะคืน True ถ้าไม่อยู่ จะคืน False
        if distance(self.x,self.y,px,py) <= self.r:
            return True
        return False
    def line_in_circle(self,line):
    # คืน True ถ้า “ส่วนของเส้นตรง” ตัด ซ้อนทับ หรือสัมผัสวงกลม นอกจากนั้นให้คืน False
        if self.contain_point(line.x1, line.y1) or self.contain_point(line.x2, line.y2): # ถ้าจุดปลายของ “ส่วนของเส้นตรง” ซักข้างอยู่ในวงกลม ให้คืนค่า True
            return True
        ret = self.line_intersection(line) # หาค าตอบว่า “เส้นตรง” ตัดกับวงกลมกี่จุด
        if ret[0] == 0: # ผลเฉลยของสมการบอกว่า ไม่มีจุดตัดของวงกลมกับ “เส้นตรง” แสดงว่าไม่มีจุดตัดกับ “ส่วนของเส้นตรง” ด้วย
            return False
        if ret[0] == 1: # ผลเฉลยของสมการบอกว่า “เส้นตรง” สัมผัสวงกลม 1 จุด
        # ให้เช็คด้วยว่าจุดนั้นอยู่ใน “ส่วนของเส้นตรง” หรือไม่ ถ้าอยู่ให้คืนค่า True ถ้าไม่อยู่ให้คืนค่า False
            return line.contain_point(ret[1][0], ret[1][1])
        if ret[0] == 2: # ผลเฉลยของสมการบอกว่า “เส้นตรง” ตัดวงกลม 2 จุด
            # ให้เช็คด้วยว่าใน 2 จุดนั้น มีซักจุดอยู่ใน “ส่วนของเส้นตรง” หรือไม่ ถ้าอยู่ให้คืนค่า True ถ้าไม่อยู่ให้คืนค่า False
            return line.contain_point(ret[1][0], ret[1][1]) or line.contain_point(ret[2][0], ret[2][1])
def distance(x1,y1,x2,y2):
 # หาระยะห่างระหว่างจุดสองจุด
    return ((x1-x2)**2+(y1-y2)**2)**0.5
class Line:
    def __init__(self,x1,y1,x2,y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    def contain_point(self,px,py):
    # คืน True ถ้าจุดอยู่บน “ส่วนของเส้นตรง” คืน False ถ้าจุดไม่อยู่บน “ส่วนของเส้นตรง”
        if not (min(self.y1,self.y2) <= py <= max(self.y1,self.y2)):
            return False
        if self.x1 == self.x2:
            return px == self.x1
        else:
            return abs((self.y1-py)*(self.x2-self.x1)-(self.y2-self.y1)*(self.x1-px))<1e-5
# ส่วนของโปรแกรมหลัก
n = int(input().strip())
line_input = [int(e) for e in input().strip().split()]
line = Line(*line_input)
output = []
for i in range(n):
    circle_input = [int(e) for e in input().strip().split()]
    circle = Circle(*circle_input)
    if circle.line_in_circle(line): # ”ส่วนของเส้นตรง” ตัดหรือสัมผัสวงกลม
        output.append(circle.index) # เติมหมายเลขวงกลมลงใน output
if len(output) == 0:
    print('Not Found')
else:
    print(' '.join([str(e) for e in output]))

#V4 __________________________________________
# I use union-find algorithm :D
class Circle:
    def __init__(self,x,y,r,color):
        self.x = x
        self.y = y
        self.r = r
        self.color = color

    def contain_point(self,px,py):
        return distance(self.x,self.y,px,py) <= self.r
    def touch(self,other):
        return distance(self.x, self.y, other.x, other.y) <= self.r + other.r
    def area(self):
        return self.r**2
    def colorw(self):
        return self.color*self.area()

def distance(x1, y1, x2, y2):
    return ((x1-x2)**2 + (y1-y2)**2)**.5

def find_root(x): #union find
    if p[x] == x:
        return x
    p[x] = find_root(p[x])
    return p[x]

def find_color(ls):
    return sum(c.colorw() for c in ls)/sum(c.area() for c in ls)

clusters = {}
n = int(input())
x, y = [float(e) for e in input().split()]
p = list(range(n))
circles = [Circle(*map(float, input().split())) for i in range(n)]
for i in range(n):
    for j in range(i):
        if circles[i].touch(circles[j]) and find_root(i) != find_root(j):
            p[find_root(j)] = find_root(i)
for i in range(n):
    p[i] = find_root(i)
    if p[i] not in clusters:
        clusters[p[i]] = []
    clusters[p[i]].append(circles[i])

ind = -1
for i in range(n):
    if circles[i].contain_point(x, y):
        ind = p[i]
        break
print(find_color(clusters[ind]) if ind!=-1 else 1.0)

#L1 _________________________________________
print('cddcc'[int(input())-1])

#L2 _________________________________________
class rint:
    def __init__(self, r):
        self.repr = r
    def __lt__(self, rhs):
        return int(self) < int(rhs)
    def __str__(self):
        return str(int(self))[::-1]
    def __int__(self):
        return int(self.repr[::-1])
    def __add__(self, rhs):
        return rint(str(int(self)+int(rhs))[::-1])
t, r1, r2 = input().split()
a = rint(r1); b = rint(r2)
if t == '1' : print(a < b)
elif t == '2' : print(int(a),int(b))
elif t == '3' : print(str(a),str(b))
elif t == '4' : print(int(a + b)) 
else : print(str(a + b))


#L3 _________________________________________
class Complex:
    def __init__(self, a, b):
        self.r = a
        self.i = b
    
    def __str__(self):
        if self.i == 0:
            return str(self.r)
        else :
            res = '${}{:+}i'.format(self.r, self.i)
            res = res.replace('+1i', '+i')
            res = res.replace('-1i', '-i')
            res = res.replace('$0+', '$')
            res = res.replace('$0-', '$-')
            return res[1:]
    def __add__(self, rhs):
        return Complex(self.r+rhs.r, self.i+rhs.i)
    
    def __mul__(self, rhs):
        a, b, c, d = self.r, self.i, rhs.r, rhs.i
        return Complex(a*c-b*d, a*d+b*c)
    def __truediv__(self, rhs):
        a, b, c, d = self.r, self.i, rhs.r, rhs.i
        return Complex((a*c+b*d)/(c**2+d**2), (-a*d+b*c)/(c**2+d**2))

t, a, b, c, d = [int(x) for x in input().split()]
c1 = Complex(a,b)
c2 = Complex(c,d)
if t == 1 : print(c1)
elif t == 2 : print(c2)
elif t == 3 : print(c1+c2)
elif t == 4 : print(c1*c2) 
else : print(c1/c2)

#L4 _________________________________________
class piggybank:
    def __init__(self):
        self.coins = {}
        self.coins_count = 0
        
    def add(self, v, n):
        if n+self.coins_count > 100:
            return False
        else:
            v = float(v)
            if v not in self.coins:
                self.coins[v] = 0
            self.coins[v] += n
            self.coins_count += n
            return True
     
    def __float__(self):
        return float(sum(key*val for key, val in self.coins.items()))
    
    def __str__(self):
        return '{' +  ', '.join('{}:{}'.format(key, val) for key, val in sorted(self.coins.items())) + '}'
        
        
cmd1 = input().split(';')
cmd2 = input().split(';')
p1 = piggybank(); p2 = piggybank()
for c in cmd1: eval(c)
for c in cmd2: eval(c)

#P1 _________________________________________
class ComplexNum:
    def __init__(self,re,im):
        self.re = re
        self.im = im
    
    def __str__(self):
        if self.im >= 0:
            return str(self.re) + '+' + str(self.im) + 'i'
        return str(self.re) + str(self.im) + 'i'
    def absolute(self):
        ab = (self.re**2+self.im**2)**0.5
        return round(ab,2)
    def __add__(self,other):
        return ComplexNum(self.re+other.re,self.im+other.im)
    def conjugate(self):
        return ComplexNum(self.re, -self.im)
     
a,b,c,d = [int(e) for e in input().strip().split()]
c1 = ComplexNum(a, b)
c2 = ComplexNum(c, d)
print(c1, c1.conjugate(), c1.absolute())
print(c2, c2.conjugate(), c2.absolute())
print(c1 +c2)


#P2 _________________________________________
def gcd(x,y):
    if x%y == 0: return y
    return gcd(y,x%y)
class Fraction:
    def __init__(self,a,b):
        self.numer = a
        self.denom = b
    
    def __str__(self):
        return '%d/%d'%(self.numer, self.denom)
    def simplify(self):
        g = gcd(self.numer,self.denom)
        return Fraction(self.numer//g,self.denom//g)
    def add(self,other):
        return Fraction(self.numer*other.denom+self.denom*other.numer, self.denom*other.denom).simplify()
    def multiply(self,other):
        ans_numer = self.numer * other.numer
        ans_denom = self.denom * other.denom
        return Fraction(ans_numer,ans_denom).simplify()
a,b,c,d = [int(e) for e in input().strip().split()]
fraction1 = Fraction(a,b)
fraction2 = Fraction(c,d)
print(fraction1.add(fraction2))
print(Fraction.multiply(fraction1,fraction2))


#P3 _________________________________________
class Card:
    def __init__(self, value, suit):
        self.v = value
        self.s = suit
    def __str__(self):
        return '(%s %s)'%(self.v,self.s)
    def getScore(self):
        v = self.v 
        if v.isdigit():
            return int(v)
        elif v == 'A':
            return 1
        return 10
    def sum(self, other):
        return (self.getScore() + other.getScore())%10
    def __lt__(self, other):
        sc = ['3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '2']
        su = ['club', 'diamond', 'heart', 'spade']
        return (sc.index(self.v), su.index(self.s)) < (sc.index(other.v), su.index(other.s))
n = int(input())
cards = []
for i in range(n):
    value, suit = input().split()
    cards.append(Card(value, suit))
for i in range(n):
    print(cards[i].getScore())
print("----------")
for i in range(n-1):
    print(Card.sum(cards[i], cards[i+1]))
print("----------")
cards.sort()
for i in range(n):
    print(cards[i])


#P4 _________________________________________
suits = ['club', 'diamond', 'heart', 'spade']
values = ['3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '2']
class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.order = 4*values.index(self.value) + suits.index(self.suit)
    def __str__(self):
        return '(%s %s)'%(self.value, self.suit)
    def next1(self):
        v1= (self.order+1)%52
        suit = suits[v1%4]
        value = values[v1//4]
        return Card(value, suit)
    def next2(self):
        self.order = (self.order+1)%52
        self.suit = suits[self.order%4]
        self.value = values[self.order//4]
n = int(input())
cards = []
for i in range(n):
    value, suit = input().split()
    cards.append(Card(value, suit))
for i in range(n):
    print(cards[i].next1())
print("----------")
for i in range(n):
    print(cards[i])
print("----------")
for i in range(n):
    cards[i].next2()
    cards[i].next2()
    print(cards[i])

#P5 _________________________________________
class Point:     
    def __init__(self, x, y):         
        self.x = x         
        self.y = y     
    def __str__(self):         
        return "("+str(self.x)+","+str(self.y)+")" 
class Rect:     
    def __init__(self, p1, p2):         
        self.ll = p1           
        self.ur  = p2       
    def area(self):         
        return (self.ur.x-self.ll.x)*(self.ur.y-self.ll.y)
    def contains(self, p):         
        ll = self.ll
        ur = self.ur
        return ll.x <= p.x <= ur.x and ll.y <= p.y <= ur.y

x1,y1,x2,y2 = [int(e) for e in input().split()] 
lowerleft = Point(x1,y1) 
upperright = Point(x2,y2) 
rect = Rect(lowerleft, upperright) 
print(rect.area()) 
m = int(input()) 
for i in range(m):     
    x,y = [int(e) for e in input().split()]     
    p = Point(x,y)     
    print(rect.contains(p))


#P6 _________________________________________
class Point: 
 def __init__(self, x, y): 
   self.x = x 
   self.y = y 
 def __str__(self): 
        return "("+str(self.x)+","+str(self.y)+")" 
class Rect: 
    def __init__(self, p1, p2): 
        self.lowerleft = p1 
        self.upperright = p2 
    def __str__(self): 
        return str(self.lowerleft)+"-"+str(self.upperright)         
    def area(self):
        return (self.upperright.x-self.lowerleft.x)*(self.upperright.y-self.lowerleft.y)
    def __lt__(self, rhs):
        return self.area() < rhs.area()

n = int(input()) 
rects = [] 
for i in range(n): 
    x1,y1,x2,y2 = [int(e) for e in input().split()]
    rects.append(Rect(Point(x1,y1), Point(x2,y2))) 
rects.sort()
for i in range(n): 
    print(rects[i])


#P7 _________________________________________
class piggybank:
    def __init__(self):
    #มีตัวแปร 4 ตัวเก็บจ านวนเหรียญของเหรียญแต่ละแบบ
        self.cnt = [0]*4
        self.value = 0

    def add1(self, n):
        self.cnt[0] += n
        self.value += n

    def add2(self, n):
        self.cnt[1] += n
        self.value += 2*n

    def add5(self, n):
        self.cnt[2] += n
        self.value += 5*n

    def add10(self, n):
        self.cnt[3] += n
        self.value += 10*n

    def __int__(self):
        return self.value

    def __lt__(self, rhs):
        return self.value < rhs.value

    def __str__(self):
        d = [1, 2, 5, 10]
        return '{' + ', '.join("%d:%d"%(d[i], self.cnt[i]) for i in range(4)) + '}'

cmd1 = input().split(';')
cmd2 = input().split(';')
p1 = piggybank() 
p2 = piggybank()
for c in cmd1: eval(c)
for c in cmd2: eval(c)


#P8 _________________________________________
#same as L4
class piggybank:
    def __init__(self):
        self.coins = {}
        self.coins_count = 0
        
    def add(self, v, n):
        if n+self.coins_count > 100:
            return False
        else:
            v = float(v)
            if v not in self.coins:
                self.coins[v] = 0
            self.coins[v] += n
            self.coins_count += n
            return True
     
    def __float__(self):
        return float(sum(key*val for key, val in self.coins.items()))
    
    def __str__(self):
        return '{' +  ', '.join('{}:{}'.format(key, val) for key, val in sorted(self.coins.items())) + '}'
        
        
cmd1 = input().split(';')
cmd2 = input().split(';')
p1 = piggybank(); p2 = piggybank()
for c in cmd1: eval(c)
for c in cmd2: eval(c)

#P9 _________________________________________
class rational:
    def __init__(self, n, d):
        self.n = n
        self.d = d
    def __str__(self):
        return str(self.n) + "/" + str(self.d)

    def __lt__(self, rhs):
        return float(self) < float(rhs)

    def __float__(self):
        return self.n / self.d

    def __mul__(self, rhs):
        return rational(self.n*rhs.n,self.d*rhs.d)

    def __add__(self, rhs):
        n1, d1, n2, d2 = self.n, self.d, rhs.n, rhs.d
        return rational(n1*d2+n2*d1, d1*d2)

    def __sub__(self, rhs):
        n1, d1, n2, d2 = self.n, self.d, rhs.n, rhs.d
        return rational(n1*d2-n2*d1, d1*d2)

    def __truediv__(self, rhs):
        n1, d1, n2, d2 = self.n, self.d, rhs.n, rhs.d
        return rational(n1*d2, n2*d1)
t, n1, d1, n2, d2 = input().split()
r1 = rational(int(n1),int(d1)); 
r2 = rational(int(n2),int(d2))
if   t == '+' : print(float(r1 + r2))
elif t == '-' : print(float(r1 -r2))
else :print(float(r1 / r2))
#P10 _________________________________________
def gcd(x, y):
    if x%y == 0:
        return y
    return gcd(y, x%y)

class rational:
    def __init__(self, n, d):
        self.n = n
        self.d = d
    def __str__(self):
        return str(self.n) + "/" + str(self.d)

    def __lt__(self, rhs):
        return float(self) < float(rhs)

    def __float__(self):
        return self.n / self.d

    def __mul__(self, rhs):
        return rational(self.n*rhs.n,self.d*rhs.d).simplifly()

    def __add__(self, rhs):
        n1, d1, n2, d2 = self.n, self.d, rhs.n, rhs.d
        return rational(n1*d2+n2*d1, d1*d2).simplifly()

    def __sub__(self, rhs):
        n1, d1, n2, d2 = self.n, self.d, rhs.n, rhs.d
        return rational(n1*d2-n2*d1, d1*d2).simplifly()

    def __truediv__(self, rhs):
        n1, d1, n2, d2 = self.n, self.d, rhs.n, rhs.d
        return rational(n1*d2, n2*d1).simplifly()


    def simplifly(self):
        g = gcd(self.n, self.d)
        self.n //= g
        self.d //= g
        return self

t, n1, d1, n2, d2 = input().split()
r1 = rational(int(n1),int(d1));
r2 = rational(int(n2),int(d2))
if   t == '+' : print(str(r1 + r2))
elif t == '-' : print(str(r1 -r2))
elif t == '/' :print(str(r1 / r2))
else          : print(str(r1 * r2))
#P11 _________________________________________
ss = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
vv = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
ll = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]
d2 = list(filter(lambda x:x[2] == 2, zip(ss, vv, ll)))
d1 = list(filter(lambda x:x[2] == 1, zip(ss, vv, ll)))
d = list(zip(vv, ss))
class roman:
    def __init__(self, r):
        self.val = 0
        if type(r) is int or r.isdigit():
            self.val = int(r)
            return 
        while r:
            for st, va, __ in d2:
                if r[:2] == st:
                    self.val += va
                    r = r[2:]
                    break
            else:
                for st, va, __ in d1:
                    if r[:1] == st:
                        self.val += va
                        r = r[1:]
                        break

    def __lt__(self, rhs):
        return self.val < rhs.val
    def __str__(self):
        s = ''
        v = self.val
        for vv, ss in d:
            while v >= vv:
                v -= vv
                s += ss
        return s

    def __int__(self):
        return self.val
    def __add__(self, rhs):
        return roman(self.val + rhs.val)


t, r1, r2 = input().split() 
a = roman(r1); 
b = roman(r2) 
if   t == '1' : print(a < b)
elif t == '2' : print(int(a),int(b)) 
elif t == '3' : print(str(a),str(b)) 
elif t == '4' : print(int(a + b))  
else          : print(str(a + b))
#P12 _________________________________________

