# basic program
def solve_01_V1():
	print('ebebb'[int(input())-1])

def solve_01_V2():
	from math import sin, pi
	a,b,c = [float(input()) for i in range(3)]
	print('area =', 0.5*a*b*sin(c*pi/180), '(sq cm)')

def solve_01_V3():
	h1, m1, s1, h2, m2, s2 = [int(input()) for i in range(6)]
	dt = 3600*(h2-h1) + 60*(m2-m1) + s2-s1
	print("%d:%d:%d"%(dt//3600 ,dt//60%60, dt%60))

def solve_01_V4():
	from math import sqrt, log10
	w, h = [float(input()) for i in range(2)]
	print(sqrt(w*h)/60,   0.024265 * w**0.5378 * h**0.3964,   0.0333 * w**(0.6157 - 0.0188*log10(w)) * h**0.3,sep='\n')

def solve_01_L1():
	print('beebd'[int(input())-1])

def solve_01_L2():
	from math import radians, cos, sqrt
	a, b, angle = [float(input()) for i in range(3)]
	print('c = {} cm.'.format(sqrt(a**2 + b**2 - 2*a*b*cos(radians(angle)))))

def solve_01_l3():
	h1, m1, s1, h2, m2, s2 = [int(input()) for i in range(6)]
	dt = (3600*(h2-h1) + 60*(m2-m1) + s2-s1 + 86400)%86400
	print("%d:%d:%d"%(dt//3600 ,dt//60%60, dt%60))

def solve_01_L4():
	number = input().strip()
	print((11-sum((13-i)*int(c) for i,c in enumerate(number))%11)%10)

def solve_01_P1():
	a, b = [int(input()) for i in range(2)]
	print(a+b, a-b, a*b, a/b, a//b, a%b, a**b, sep='\n')

def solve_01_P2():
	print(3.14159*float(input())**2)

def solve_01_P3():
	print(sum(float(input()) for __ in range(5))/5)

def solve_01_P4():
	x = float(input())
	print(x**2/2, 	x**3/6, 	x**4/24, 	1+x+x**2/2+x**3/6+x**4/24, sep='\n')

def solve_01_P5():
	a, b, c = [float(input()) for i in range(3)]
	rdis = (b**2-4*a*c)**0.5
	print('x1 = {}\nx2 = {}'.format((-b+rdis)/a*0.5, (-b-rdis)/a*0.5))

def solve_01_P6():
	a1, b1, c1 = [float(x) for x in input().strip().split()]
	a2, b2, c2 = [float(x) for x in input().strip().split()]
	c1, c2 = -c1, -c2
	det0 = a1*b2 - a2*b1
	det1 = c1*b2 - c2*b1
	det2 = a1*c2 - a2*c1
	print(det1/det0,det2/det0)

def solve_01_P7():
	c = float(input())
	print(1.8*c + 32, c+273.15)

def solve_01_P8():
	w, h = int(input()), int(input())
	print(w/(h/100)**2)

def solve_01_P9():
	a, b, c = [int(x) for x in input().split()]
	p = (a+b+c)/2
	print((p*(p-a)*(p-b)*(p-c))**0.5)

def solve_01_P10():
	digits = input().strip()
	print(digits + str((11-sum( (10-i)*int(x) for i,x in enumerate(digits))%11)%11))