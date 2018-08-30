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
def solve_08_V1():
    print('ceedc'[int(input())-1])

def solve_08_V2(): # -> BUG , 80 mmark
    s = [{word for word in (''.join(char if char.isalpha() else ' ' for char in open(fn).read().lower()) ).split()} for fn in ['file1.txt', 'file2.txt']]
    word = input().strip().lower()
    print(['Not found', 'Found in file1 only','Found in file2 only', 'Found in both files'][(word in s[0]) + (word in s[1])*2])


def solve_08_V3():
    from collections import defaultdict as dd
    addr = dd(lambda: ['Not found'] ,{(n, sn):(num, em) for line in open('address.txt') for n, sn, num, em in [line.split()]})

    while True:
        try:
            n, sn = input().split()
            print(*addr[(n, sn)])
        except: 
            break


def solve_08_L1():
    print('dbacd'[int(input())-1])
    # 1 --> usage: tuple(iteratable)
    # 2 --> set cannot use + operator
    # 3 --> {'c', 'd', 'e'} is same as 1)
    # 4 --> d2 refer to same dict as d1
    # 5 O(log(n)) PogChamp

def solve_08_L2():
    d = {(n, sn):num for line in open('address.txt') for n, sn, num in [line.split()]}

    while True:
        x = input().strip()
        if x.isdigit():
            print(*next((key for key, val in d.items() if val==x), ['Not Found']))
        elif x != '':
            try:   print(d[(*x.split(),)])
            except: print('Not Found')
        else: break
def solve_08_L3():
    from collections import Counter
    count = Counter(''.join( c for c in open(input().strip()).read() if c.isalnum() or c in '\n ').lower().split())
    print(sorted(count.items(), key=lambda x:(-x[1], x[0]))[:10])
    # one line
    if False:
        print(sorted(__import__('collections').Counter(''.join( c for c in open(input().strip()).read() if c.isalnum() or c in '\n ').lower().split()).items(), key=lambda x:(-x[1], x[0]))[:10])

solve_08_L3()
      

def solve_08_V4():
    data = {} #course string : set of student that enrolled to that course
    while 1:
      std, *courses= input().strip().split()
      if courses:
        for c in courses:
          if c not in data:
            data[c] = {std}
          else:
            data[c].add(std)
      else:
        break
    c1, c2 = input().strip().split()
    # also NEED to check if course doesn't exist
    s1 = data[c1] if c1 in data else set()
    s2 = data[c2] if c2 in data else set()
    print(len(s1&s2), len(s1^s2), len(s1|s2))



def solve_08_L4():
    file = open('.data.txt')
    kw2b = {} # kw --> set of book with that kw

    for num, line in enumerate(file.readlines()):
      # there's space between commas
      book, *keywords = [token.strip() for token in line.split(',')] 
      for kw in keywords:
        if kw not in kw2b:
          kw2b[kw] = {(num,book)}
        else:
          kw2b[kw].add((num, book))

    file.close()
    first, *rest = [token.strip() for token in input().split(',')]
    if first in kw2b:
        almost_ans = kw2b[first] 
    else:
        almost_ans = set()
    for kw in rest:
        if kw in kw2b:
            now = kw2b[kw]
        else:
            now = set()
        almost_ans = almost_ans&now
    ans = [name for num, name in sorted(list(almost_ans))]
    print(*ans if ans else ['Not found'], sep='\n')


def solve_08_P1():
    n = int(input())
    l2u = {}
    visited = {}
    for i in range(n):
        uid, loc = [tok.strip() for tok in input().split(':')]
        loc = [tok.strip() for tok in loc.split(',')]
        visited[uid] = loc
        for x in loc:
            if x not in l2u:
                l2u[x] = {(i, uid)} #sort by input order
            else:
                l2u[x].add((i, uid)) #sort by input order

    keyID = input().strip()
    almost_ans = set()
    for x in visited[keyID]:
        almost_ans.update(l2u[x])
    ans = sorted(list(almost_ans))

    if len(ans) == 1:
        print("Not Found")
    else:
        for (num, uid) in ans:
            if uid != keyID:
                print(uid)


def solve_08_P2():
    prog = {} # prog_id to applicant id
    n = int(input())
    for i in range(n):
        uid, *app = input().strip().split(', ')
        for a in app:
            if a not in prog:
                prog[a] = {(i, uid)}
            else:
                prog[a].add((i, uid))
    que = input().strip().split(', ')
    for x in que:
        if x not in prog:
            now = set()
        else:
            now = prog[x]
        ans = [uid for (num, uid) in sorted(list(now))]
        if ans == []:
            ans += ['Not found']
        print(x, '->', ', '.join(ans))

def solve_08_P3():
    cnt = {}
    nums = sorted([int(x) for x in input().split()])
    for x in nums:
        if x not in cnt:
            cnt[x] = 1
        else:
            cnt[x] += 1
    for x in nums:
        if cnt[x] == 1:
            print(x)
            break
    else:
        print("NONE")

def solve_08_P4():
    ls = [int(x) for x in input().split()]
    sm = int(input())
    n = len(ls)
    cnt = 0 
    for i in range(n):
        for j in range(i+1, n):
            if ls[i]+ls[j] == sm:
                cnt += 1
    print(cnt)

def solve_08_P5():
    cnt = {}
    ls = [int(x) for x in input().split()]
    n = len(ls)
    for x in ls:
        if x not in cnt:
            cnt[x] = 1
        else:
            cnt[x] += 1
    sm = int(input())
    ans = 0
    for x in cnt.keys():
        if sm-x in cnt.keys():
            ans += cnt[x]*cnt[sm-x]
    if 2*x == sm and x in cnt:
        ans -= cnt[x]
    print(ans//2)

def solve_08_P6(): # --> BUG: cant get 100
    n, q = [int(x) for x in input().split()]
    ls = [int(x) for x in input().split()]
    que = [int(x) for x in input().split()]
    cnt = {}
    for i in range(n):
        for j in range(i+1, n):
            sm = ls[i]+ls[j]
            if sm not in cnt:
                cnt[sm] = {(i, j)}
            else:
                cnt[sm].add((i,j))
    for x in que: 
        found = False
        for ind, y in enumerate(ls): # pick 1 number
            if found:
                break
            elif x-y not in cnt:
                continue
            else:
                try:
                    for possibleAns in cnt[x-y]:
                        if  ind not in possibleAns:
                            found = True
                            break
                except:
                    print("LUL")
        print('YES' if found else 'NO') 
    n, q = [int(x) for x in input().split()]
    ls = [int(x) for x in input().split()]
    que = [int(x) for x in input().split()]
    cnt = {}
    for i in range(n):
        if ls[i] not in cnt:
            cnt[ls[i]] = 1
        else:
            cnt[ls[i]] += 1
    for x in que: 
        found = False
        for i in range(n):
            if found:
                break
            for j in range(i+1, n):
                if x-ls[i]-ls[j] in cnt and cnt[x-ls[i]-ls[j]] > 2:
                    found = True
                    break
        print(["NO", "YES"][found])

def solve_08_P7():
    cnt = {}
    n = int(input())
    for i in range(n):
        inp = input().strip().split()[-1]
        x = inp[:2] 
        if x not in cnt:
            cnt[x] = {(i,inp)}
        else:
            cnt[x].add((i, inp))
    mx, mxcnt = '', 0

    for k, v in cnt.items():
        if len(v) > mxcnt:
            mxcnt = len(v)
            mx = k
        elif len(v) == mxcnt and k < mx:
            mx = k
    ans = [word for (num, word) in sorted(list(cnt[mx]))]
    print(mx, mxcnt, *ans, sep='\n')


def solve_08_P8():
    l1, l2, words = [input().strip().split() for i in range(3)]
    l1, l2 = l1+l2, l2+l1
    enc = {l1[i]:l2[i] for i in range(len(l1))}
    for i in range(len(words)):
        if words[i] in enc:
            words[i] = enc[words[i]]
    print(' '.join(words))

def solve_08_P9():
    n = int(input())
    ls = [int(input()) for i in range(n)]
    cnt = {x:ls.count(x) for x in ls}
    print(-max([(v, -k) for k, v in cnt.items()])[1])

def solve_08_P10():
    gr = {}
    yr = {}
    dp = {}
    info = {}
    ans =  set()
    grv = list('ABCEFGHJIKLMNOPQRSTUVWXYZ') + ['Dog']
    n = int(input())
    for i in range(n):
        name, group, year, dep = input().split()
        info[name] = (group, year, dep)
        ans.add((i, name))
        if group not in gr:
            gr[group] = {(i, name)}
        else:
            gr[group].add((i, name))
        if year not in yr:
            yr[year] = {(i, name)}
        else:
            yr[year].add((i, name))
        if dep not in dp:
            dp[dep] = {(i, name)}
        else:
            dp[dep].add((i, name))

    condition = input().split()
    for x in condition:
        if x in grv:
            # print('group', x)
            if x in gr:
                now = gr[x]
            else:
                now = set()
        elif x.isdigit():
            # print('year', x)
            if x in yr:
                now = yr[x]
            else:
                now = set()
        else:
            # print('dep', x)
            if x in dp:
                now = dp[x]
            else:
                now = set()
        ans = ans&now
    ans = sorted([name for (num, name) in ans])
    for nick in ans:
        print(nick, *info[nick])
    if not ans:
        print("Not Found")



def solve_08_P11():
    n = int(input())
    suggestion = [{*input().split()} for i in range(n)]
    interest = input().strip()
    cnt = {}
    found = False
    for s in suggestion:
        if interest in s:
            found = True
            for event in s:
                if event not in cnt:
                    cnt[event] = 1
                else:
                    cnt[event] += 1
    if not found:
        print('Not Found')
    elif len(cnt) <= 1:
        print('No suggested event') 
    else:
        suggested_list = list(cnt.items()) # list of (event, sugg_count) pairs
        suggested_list.sort(key=lambda x: (-x[1], x[0]))
        print(*suggested_list[1], sep='\n')


def solve_08_P12():
    n = int(input())
    suggestion = [{*input().split()} for i in range(n)]
    interest = input().strip()
    cnt = {}
    found = False
    for s in suggestion:
        if interest in s:
            found = True
            for event in s:
                if event not in cnt:
                    cnt[event] = 1
                else:
                    cnt[event] += 1
    if not found:
        print('Not Found')
    elif len(cnt) <= 1:#have only self
        print('No suggested event') 
    else:
        suggested_list = list(cnt.items()) # list of (event, sugg_count) pairs
        suggested_list.sort(key=lambda x: (-x[1], x[0]))
        print(*("%s %d"%(name, cnt) for name, cnt in suggested_list[1:]), sep='\n')

def solve_08_P13():
    adj = {}
    while True:
        st, st2, *_ = input().split() + ['']*2
        if st2 == '':
            ans = {st}
            ans.update({dest for start in ans for dest in (adj[start] if start in adj else [])})
            ans.update({dest for start in ans for dest in (adj[start] if start in adj else [])})
            print(*sorted(ans), sep='\n')
            break
        else:
            if st not in adj: adj[st] = {st2}
            else: adj[st].add(st2)
            if st2 not in adj: adj[st2] = {st}
            else: adj[st2].add(st)


def solve_08_P14():
    avaiable_seat = {}
    chosen_dept= {}
    students = []
    n = int(input())
    for i in range(n):
        data = input().split()
        avaiable_seat[data[0]] = int(data[1])

    n = int(input())
    for i in range(n):
        sid, score, *preferences = input().split()
        students.append([sid, float(score), preferences])
    students.sort(key=lambda x:x[1], reverse=True)

    for sid, score, preferences in students:
        for dept in preferences:
            if avaiable_seat[dept] > 0:
                avaiable_seat[dept] -= 1
                chosen_dept[sid] = dept
                break
    print(*(' '.join(std) for std in sorted(chosen_dept.items())),sep='\n')


def solve_08_P15():
    courses = {}
    teachers = {}
    file1 = open(input().strip())
    for line in file1:
        ref, cid = line.strip().split(',')
        courses[ref] = cid
    file1.close()

    file2 = open(input().strip())
    for line in file2:
        ref, tid = line.strip().split(',')
        teachers[ref] = tid
    file2.close()

    file3 = open(input().strip())
    for line in file3:
        cref, tref = line.strip().split(',')
        if cref in courses and tref in teachers:
            print("%s,%s"%(courses[cref], teachers[tref]))
        else:
            print('record error')


def solve_08_P16():
    n = int(input())
    ans_union = {int(x) for x in input().split()} 
    ans_intersection = set(ans_union)
    for i in range(1, n):
        now = {int(x) for x in input().split()}
        ans_union |= now
        ans_intersection &= now
    print(len(ans_union), len(ans_intersection),sep='\n')


def solve_08_P17():
    n = int(input())
    all_team = set()
    lose_team = set()
    for i in range(n):
        winner, loser = input().split()
        all_team.update({winner, loser })
        lose_team.add(loser)
    print(sorted(all_team-lose_team))
# ---------------- LOOOL 4HEad -----------------
if sublime:
    __OMEGALUL__.close()
if tofile and sublime:
    __LUL3D___.close()
# ----------------------------------------------