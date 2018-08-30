# _________ Sample_Q3_2 ___________________________
from numpy import array, dot, shape
m, n, p = map(int, input().split())
m1 = array([[int(c) for c in input().split()] for i in range(m)], int)
m2 = array([[int(c) for c in input().split()] for i in range(n)], int)
res = m1.dot(m2)
if len(shape(res)) == 2:
  print(*[*map(lambda x: ' '.join(map(str, x)), res)], sep='\n')
else:
  print(*res)

# _________ Sample_Q3_3 ___________________________
from collections import defaultdict as dd
page_likers = {}
liked_pages = {}
n = int(input())
for i in range(n):
    name, *pages = input().strip().split()
    if name not in liked_pages:
        liked_pages[name] = set()
    liked_pages[name].update(pages)
    for p in pages:
        if p not in page_likers:
            page_likers[p] = set()
        page_likers[p].add(name)
while True:
    c1, c2, *arg = input().strip().split() + ['']*2
    if c1 == 'exit': break
    elif c1 == 'common':
        if c2 == 'page':
            ans = set(page_likers.keys()) # all possible pages
            for person in arg[:-2]: # don't want last 2 ''
                if person not in liked_pages.keys():
                    ans &= set()
                    break
                ans &= liked_pages[person]
            print(len(ans))
        elif c2 == 'user':
            ans = set(liked_pages.keys()) # all possible person
            for page in arg[:-2]: # don't want last 2 ''
                if page not in page_likers.keys():
                    ans &= set()
                    break
                ans &= page_likers[page]
            print(len(ans))
    elif c1 == 'similar':
        if c2 == 'user':
            this = arg[0]
            if this not in liked_pages.keys():
                print(min(liked_pages.keys()))
            else:
                print(min((-len(liked_pages[this]&liked_pages[user])/len(liked_pages[this]|liked_pages[user]), user)  
                    for user in liked_pages.keys() if user != this)[1])
        elif c2 == 'page':
            this = arg[0]
            if this not in page_likers.keys():
                print(min(page_likers.keys()))
            else:
                print(min((-len(page_likers[this]&page_likers[page])/len(page_likers[this]|page_likers[page]), page)  
                    for page in page_likers.keys() if page != this)[1])



# _________ Sample_Q3_4 ___________________________
arr = []
while True:
    mask, *people = input().strip().split() + ['']
    if mask == 'end': break
    people = people[:-1]
    for x in arr:
        if x[0] == mask:
            for p in people:
                if p not in x[1]:
                    x[1].append(p)
            break
    else:
        pu  = []
        for p in people:
          if p not in pu:
            pu.append(p)
        arr.append((mask, pu, len(arr)))
while arr:
  arr.sort(key=lambda x:(len(x[1]), x[2]))
  mask, p = arr[0][0], arr[0][1][0]
  print(mask, p)
  del arr[0]
  for m in arr:
      if p in m[1]:
          m[1].remove(p)



# _________ Sample_Q4_2a ___________________________
import numpy as np
def H(n):
  if n == 1:
    return np.ones((1,1), int)
  size = 2**(n-1)
  prev = H(n-1)
  ans = np.zeros((size, size), int)
  ans[0:size//2, 0:size//2] = ans[size//2:size, 0:size//2] = \
  ans[0:size//2, size//2:size] = ans[size//2:size, size//2:size] = prev
  ans[size//2:size, size//2:size] *= -1
  return ans

def P(n):
  return 1 if n == 1 else 3*P(n-1) + M(n-1)

def M(n):
  return 0 if n == 1 else 3*M(n-1) + P(n-1)

def S(n):
  return P(n)-M(n)

exec(input().strip()) # do not remove this line


# _________ Sample_Q4_2b ___________________________
def F(n):
  if n<3:
    return [0, 1, 1][n] 
  else:
    if n%3 == 0:
      m = n//3
      k = F(m)
      return 5*k**3+3*(-1)**m*k
    elif n%3 == 1:
      m = n//3
      k = F(m+1)
      p = F(m)
      return k**3 + 3*k*p**2 - p**3
    elif n%3 == 2:
      m = n//3
      k = F(m+1)
      p = F(m)
      return k**3 + 3*k**2*p + p**3
  
def x(m, n):
  if m==0 or n==0:
    return m+n
  else:
    return x(m-1, n)+x(m, n-1)

def p(n):
  if n <= 1:
    return n
  a, b = p(0), p(1)
  for i in range(2, n+1):
    if i%2 == 0:
      a, b = b, i+2*b + a
    else:
      a, b = b, i + b + 2*a
  return b
  
def z1(n):
  k = z2(n)
  return z1(k) + k if n>=10 else k

def z2(n):
  return n%10 + z2(n//10) if n>=10 else n
  
exec(input().strip())  # do not remove this line



# _________ Sample_Q4_3 ___________________________
symbol= '0123456789+-,./!'

def remove_symbol(s):
    return ''.join(' ' if c in symbol else c for c in s).lower()

def str_to_unique_list(s):
    k = s.strip().split()
    ans = list()
    for x in k:
        if x not in ans: ans.append(x)
    return ans

def percent_in_list(template, test):
    set1 = template
    set2 = test
    return sum(1 for x in set1 if x in set2)*100/len(set2)

def main():
    good = remove_symbol(input().strip())
    good_list = str_to_unique_list(good)
    bad = remove_symbol(input().strip())
    bad_list = str_to_unique_list(bad)
    n = int(input())
    for i in range(n):
        test = remove_symbol(input().strip())
        test_list = str_to_unique_list(test)
        good_p = percent_in_list(good_list, test_list)
        bad_p = percent_in_list(bad_list, test_list)

        print(test_list)
        print(good_p, bad_p)

exec(input().strip())# do not remove this line




# _________ Sample_Q4_4 ___________________________
import numpy as np

def read_matrix():
    r,c = [int(e) for e in input().split()]
    m = [[int(e) for e in input().split()] for i in range(r)]
    return np.array(m)

def dot_row_column(m):
    return m.dot(m)

def mul_submatrix(m, n):
    x = np.array(m)
    r, c = x.shape
    k  = n.shape[0]
    for i in range(0, r, k):
        for j in range(0, c, k):
            x[i:i+k, j:j+k] = x[i:i+k, j:j+k].dot(n)
    return x

def resize(m, a, b):
    ans = np.zeros((a, b), type(m[0][0]))
    r, c = m.shape
    """
    [...... ...... ...... +++++]
    [...... ...... ...... +++++]
    [...... ...... ...... +++++]
    [...... ...... ...... +++++]
    [...... ...... ...... +++++]
    [...... ...... ...... +++++]
    [------ ------ ------ *****]
    [------ ------ ------ *****]

    """
    for i in range(0, a//r*r, r):
        for j in range(0, b//c*c, c):
            ans[i:i+r, j:j+c] = m
            p, q= i, j
    p = a//r*r
    q = b//c*c
    if a%r != 0:
        for j in range(0,  b//c*c, c):
            ans[p:a, j:j+c] = m[0:((a-1)%r+1), :]
    if b%c != 0:
        for i in range(0, a//r*r, r):
            ans[i:i+r, q:b] = m[:, 0:((b-1)%c+1)]
    if a%r != 0 and b%c != 0:
        ans[p:a, q:b] = m[0:((a-1)%r+1), 0:((b-1)%c+1)]
    return ans

exec(input().strip())# do not remove this line




# _________ 59_2_Q3_2_p ___________________________
ls = sorted(list(map(int, input().split())))
n = len(ls)
k = int(input())
if k>ls[-1]: print('Too tall')
elif k<ls[0]: print('Too short')
else:
    print("{}th percentile".format(next((i*100/n for i in range(n) if k<ls[i]), 100.0)))


# _________ 59_2_Q3_3_p ___________________________
def print_money(s, m) :
    sorted_m = sorted([ (v, m[v]) for v in m ])
    sorted_m = sorted_m[::-1] # reverse order --> max to min
    print(s,','.join([str(v)+":"+str(c) for v,c in sorted_m if c>0]))

money = input().strip().split(",")
pocket_money = dict()
for item in money :
    v, c = [int(e) for e in item.split(":")]
    pocket_money[v] = c

print_money("In pocket:", pocket_money)
pocket_amount = sum(k*v for k, v in pocket_money.items())
pay_amount = int(input())
if pay_amount > pocket_amount :
    print("Not enough money")
else:
    pay_money = dict()
    sorted_money = sorted([ (v, pocket_money[v]) for v in pocket_money ])
    sorted_money = sorted_money[::-1] # reverse order --> max to min
    p = pay_amount
    for value,count in sorted_money :
        if value*count > p:
            c = p // value
        else :
            c = count
        p -= value*c
        pay_money[value] = c
    if p != 0 :
        print("Not match")
    else :
        print_money("Pay:", pay_money)
        for k,v in pay_money.items():
            pocket_money[k] -= v
        print_money("Left in pocket:", pocket_money)



# _________ 59_2_Q3_4_p ___________________________
n = int(input())
votes = {}
score = {}
for i in range(n):
    a, b = input().strip().split(',')
    if a not in votes:
        votes[a] = set()
    votes[a].add(b)

for voter, voted in votes.items():
    for person in voted:
        if person not in score:
            score[person] = 0
        score[person] -= 1
a = sorted((v, k) for k, v in score.items())
print(','.join(x[1] for x in a[:3]))



# _________ 59_2_Q4_2_p ___________________________
def S(n,k): 
    return 1 if n == k else \
    0 if n > 0 and k == 0 else \
    S(n-1, k-1)-(n-1)*S(n-1, k)
    
def L(x,y,i,j):       
    return 0 if i == -1 or j == -1 else \
    max(L(x, y, i-1, j), L(x, y, i, j-1)) if x[i] != y[j] else \
     1 + L(x, y, i-1, j-1)
    
def P(n,k):   # Time out alert !!!
    if n <= k:
        return k
    elif k%2 == 0:
        x = P(n, k+1)
        return 2 + x +  x%789
    else:
        return P(n, k+3) - 5
    return 0
    
def Hanoi(n,L,M,R):   
    if n == 0:
        return 
    Hanoi(n-1, L, R, M)
    print(n, L, '->', R)
    Hanoi(n-1, M, L, R)
    return 0
    
def extract_sign(t):
    sign = ''
    if t[0]=='-':
        t = t[1:]
        sign = 'lop-'
    return sign,t
def split_by_point(t):
    k = t.find('.')
    d = ''
    if k >= 0:
        d = t[k+1:]
        t = t[:k]
    return t,d
def remove_comma(t):
    return t.replace(',','')

def split_by_million(t):
    tm = ''
    if len(t) > 6 :
        tm = t[:-6]
        t = t[-6:]
    return tm,t
def digit_to_text(d):
    digits = 'soon nuengsong sam  see  ha   hok  jed  pad  kao  '
    return digits[d*5:d*5+5].strip()
def pos_to_text(p):
    pos = '    sip roeypun muensaenlarn'
    return pos[p*4:p*4+4].strip() 
def number_to_text(t):
    out = ''
    for p in range(len(t)):
        d = t[len(t)-p-1]
        if d == '0' : continue
        tmp = digit_to_text(int(d)) + '-' + pos_to_text(p)
        if p == 0 :
            out = tmp
        else:
            out = tmp + '-' + out
    out = out[:-1]
    if out[-5:] == '-soon' : out = out[:-5]
    out = out.replace('song-sip', 'yee-sip')
    out = out.replace('nueng-sip', 'sip')
    out = out.replace('sip-nueng', 'sip-ed')
    return out
def combine(moreM, lessM):
    out = lessM
    if   moreM == '' and lessM == '' : out = 'soon'
    elif moreM != '' and lessM == '' : out = moreM + '-larn' 
    elif moreM != '' and lessM != '' : out = moreM + '-larn-' + lessM 
    return out
def num2th(num):
    sign,num     = extract_sign(num)
    leftJ,rightJ = split_by_point(num)
    leftJ        = remove_comma(leftJ)
    moreM,lessM  = split_by_million(leftJ)
    tLessM       = number_to_text(lessM)
    tMoreM       = number_to_text(moreM)
    out          = combine(tMoreM, tLessM)
    if rightJ != '' :
        out += '-jood'
        for d in rightJ:
            out += '-' + digit_to_text(int(d))
    print(sign + out)
   
exec(input().strip()) # do not remove this line



# _________ 59_2_Q4_3_p ___________________________
import numpy as np

def to_polar(p):
    X,Y = p[:,0], p[:,1]
    rt = np.ndarray(p.shape)
    rt[:,0] = np.sqrt(X**2+Y**2)
    rt[:,1] = np.arctan2(Y,X)
    return rt

def to_cartesian(p):
    R,T = p[:,0], p[:,1]
    xy = np.ndarray(p.shape)
    xy[:,0] = R*np.cos(T)
    xy[:,1]= R*np.sin(T)
    return xy

def mandel(h, w, m):
    y,x = np.ogrid[ -1.4:1.4:h*1j, -2:0.8:w*1j ]
    c = x+y*1j
    z = c
    dt = m + np.zeros(z.shape, dtype=int)
    for i in range(m):
        z = z**2 + c
        di = z*np.conj(z) > 2**2         
        dn= di & (dt==m)  
        dt[dn] = i                  
        z[di] = 2  
    return dt


def merge(dt,m):
    x = dt[m,:]
    y = dt[:,m]
    xy = [[x[k],y[k]] for k in range(len(x))]
    xy = np.array(xy,float)
    return xy

def main():
    h1,w1,m1 = [int(e) for e in input().split()]
    h2,w2,m2 = [int(e) for e in input().split()]
    
    dt1 = mandel(h1, w1, m1)
    xy1= merge(dt1, m1)
    rt1 = to_polar(xy1)
    rt1[:,1] += 0.5
    xy1 = to_cartesian(rt1)
    
    dt2 = mandel(h2, w2, m2)
    pq2= merge(dt2, m2)
    pq2[:,1] += 0.5
    xy2 = to_cartesian(pq2)
    
    print(np.sum(xy1.dot(xy2.T)))



exec(input().strip()) # do not remove this line




# _________ 59_2_Q4_4_p ___________________________
import numpy as np

def decode(c, base, oddonly):
    r = c.shape[0]
    mult = np.ones((1,r))
    mult[0, 1:] *= base
    mult = np.cumprod(mult, dtype=int)
    mult = np.flip(mult, 0)
    ans = np.dot(mult, c)
    if oddonly:
      return ans[1::2]
    else:
      return ans

    

exec(input().strip()) # do not remove this line
exec(input().strip()) # do not remove this line
exec(input().strip()) # do not remove this line



# _________ 59_3_Q3_2_p ___________________________
s = [list(map(int, input().split())) for i in range(2)]
t = input().strip()
if t == 'z':
    m = min(len(s[0]), len(s[1]))
    ans = [s[i%2][i//2] for i in range(2*m)]
    if len(s[0]) > m:
        ans += s[0][m:]
    if len(s[1]) > m:
        ans += s[1][m:]
else:
    i = j = 0
    n, m=len(s[0]), len(s[1])
    ans = []
    while i<n and j<m:
        if s[0][i] < s[1][j]:
            ans.append(s[0][i])
            i += 1
        else:
            ans.append(s[1][j])
            j += 1
    while i<n:
        ans.append(s[0][i])
        i+=1
    while j<m:
        ans.append(s[1][j])
        j+=1
print(ans)




# _________ 59_3_Q3_3_p ___________________________
n = int(input())
data = []
for i in range(n):
    name, *vit = input().split()
    data.append((name, list(map(float, vit))))
cmd, *arg = input().split() + ['']
if cmd == 'show':
    for name, vit in data:
        print(name, *vit)
elif cmd == 'get':
    x = arg[0]
    for name, vit in data:
        if name == x:
            print(name, *vit)
            break
    else:
        print(x ,'not found')
elif cmd == 'avg':
    x = int(arg[0])-1
    print(round(sum(vit[x] for name, vit in data)/len(data), 4))

elif cmd == 'max':
    x = int(arg[0])-1
    tmp =  min([(-vit[x], name.lower(), name) for name, vit in data])
    print(tmp[2], -tmp[0])

elif cmd == 'sort':
    x = int(arg[0])-1
    print(*[name for name, vit in \
    sorted(data, key =lambda u: (u[1][x], u[0].lower()))])




# _________ 59_3_Q3_4_p ___________________________
q = list()
sm, x = 0, 0 #sum of waiting time, num of served customer
last_id, last_tm = 0, 0
next_num = 0
n = int(input())
for i in range(n):
  cmd, *arg = input().split() + ['']
  if cmd == 'reset':
    next_num = int(arg[0])
  elif cmd == 'new':
    tm = int(arg[0])
    q.append((next_num, tm))
    print('ticket', next_num)
    next_num += 1
  elif cmd == 'next':
    last_id, last_tm = q[0]
    q = q[1:]
    print('call', last_id)
  elif cmd == 'order':
    tm = int(arg[0])
    print('qtime', last_id, tm-last_tm)
    sm += tm-last_tm
    x += 1
  elif cmd == 'avg_qtime':
    print('avg_qtime', round(sm/x, 4))







# _________ 59_3_Q4_2_p ___________________________
def p(n):
  return 1 if n <= 2 else p(n-2) + p(n-3)

def m(n):
  if n == 1 or n == 2:
    return 1
  else:
    x = m(n-2)
    return m(x) + m(n-x)

def e(n):
  return sum(e(k+1)*e(n-k) for k in range(1, n-1)) if n > 3 else 1

def s(n, k):
  if n== 0:
    return 2
  else:
    x = s(n-1, k)
    return (x**2 - x + 1)%k

exec(input().strip())


# _________ 59_3_Q4_3_p ___________________________
def read_data():
  # read data from keyboard, add the data into dict D
  # and return dict D when done
  D = dict()
  n = int(input())# number of student’s records to read in
  for k in range(n):
    sid,name,gpax,year,dept = [e.strip() for e in input().strip().split(',')]
    gpax = float(gpax);year = int(year)
    if dept not in D :
      D[dept] = {sid:(name,gpax,year)}
    else :
      D[dept][sid] = (name,gpax,year)
  return D

def is_in(D, sid, dept):
  return sid in D.get(dept, {}).keys()

def get_year(D, sid):
  for dept in D.keys():
    if sid in D[dept].keys():
      return D[dept][sid][2]
  return False

def get_supers(D, dept):
  if dept not in D: return False
  return {sid for sid, data in D[dept].items() if data[2] > 4}

def max_gpax(D):
  return max(data[1] for dept in D.keys() for sid, data in D[dept].items())

def get_max_gpax_students(D):
  m = max_gpax(D)
  return {(sid, data[0]) for dept in D.keys() for sid, data in D[dept].items() if data[1] == m}
# do not remove the following lines!!
n = int(input())
for k in range(n):
  exec(input().strip())


  
# _________ 59_3_Q4_4_p ___________________________

# _________ 60_1_Q2_00_p ___________________________
# _________ 60_1_Q2_0a_p ___________________________
# _________ 60_1_Q2_1_p ___________________________
# _________ 60_1_Q2_2a_p ___________________________
# _________ 60_1_Q2_3_p ___________________________