def solve_04_V1():
	print('bdccb'[int(input())-1])

def solve_04_V2():
	print(''.join(' ' if c in '"\',.()' else c for c in input().strip()))

def solve_04_V3():
	s = ' ' + (''.join(' ' if c in '"\',.()' else c for c in input().strip())) + ' '
	word = ' ' + input().strip() + ' '
	print("Found" if word.lower() in s.lower() else "Not Found")

def solve_04_V4():
	s = input().strip() + ' '
	text = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
	ls = [text[int(cur)]+ (' ' if nxt.isdigit() or nxt.isalpha() else '') if cur.isdigit() else cur \
	for cur, nxt in zip(s[:-1], s[1:])]
	print(''.join(ls).strip())

def solve_04_L1():
	print(['ddedd'][int(input())-1].lower())

def solve_04_L2():
	x = input().strip().lower()
	cnt = ans = 1
	for prev, now in zip(x[:-1], x[1:]):
		cnt = cnt+1 if prev==now else 1
		ans = max(ans, cnt)
	print(ans)

def solve_04_L3():
	x, y = input().strip(), input().strip()
	xl, yl = x.lower(), y.lower()
	print(x if all(xl.count(c) == yl.count(c) for c in 'qwertyuiopasdfghjklzxcvbnm') else ' '.join([x, y]))

def solve_04_L4():
	mode, orig, find, repl = [input().strip() for i in range(4)]
	out = ''
	found_index = s.lower().find(find_string.lower())
	while found_index >= 0:
		out += s[:found_index] + replace_string
		s = s[found_index+len(find_string):]
		if mode == 'R':
			break
		found_index = s.lower().find(find_string.lower())
	print(out+s)

def solve_04_P1():
	print(sum(1 for c in input().strip() if c.isupper())) # one line btw haHAA

def solve_04_P2():
	x = input().strip().lower()
	cons_cnt = sum(1 for c in x if c in 'bcdfghjklmnpqrstvwxyz')
	vow_cnt = sum(1 for c in x if c in 'aeiou')
	print(vow_cnt, cons_cnt)
	# idea: could use alpabet_count - vowels_count too!

def solve_04_P3():
	x, y = [a for a in input().strip().split()]
	print(x.capitalize(), sum(int(u) for u in y if u.isdigit()))

def solve_04_P4():
	m, d, y = [x for x in input().strip().split('/')] 
	print(d, 'JANFEBMARAPRMAYJUNJULAUGSEPOCTNOVDEC'[3*(int(m)-1):3*int(m)], y)

def solve_04_P5():
	x = input().strip() 
	print(x + str(sum(1 for c in x if c == '1')%2))

def solve_04_P6():
	x = input().strip() 
	print(x + str(sum(1 for c in x if c == '1')%2))

def solve_04_P7():
	s = input().strip()
	ls = [d for d in '0123456789' if d not in s]
	print(*ls if ls else ['No missing digits'])

def solve_04_P8():
	x = input().strip().lower()
	print("no" if any(x[i] < x[i-1] for i in range(1, len(x))) else "yes")
	 
def solve_04_P9():
	s, a, b = [input().strip() for i in range(3)] 
	print(*[next((repl for find, repl in zip(a+b,b+a) if char == find), char) for char in s], sep='')

def solve_04_P10():
	s, a, b = [input().strip() for i in range(3)] 
	print(*[next((repl for find, repl in zip(a+b,b+a) if char == find), char) for char in s], sep='')

def solve_04_P11():
	x  = input().strip()
	a, b = (int(u) for u in input().strip().split())
	print(x[:a] + x[a:b+1][::-1] + x[b+1:])

def solve_04_P12():
	x = input().strip().lower().replace(' ', '')
	print('yes' if x==x[::-1] else 'no')
	# krist -> ['yes', 'n'][x==x[::-1]] --> f**King genius

def solve_04_P13():
	x = input().strip() + 'q'
	print(sum(1 for i in range(len(x)-1) if x[i] in 'aeiou' and x[i+1] not in 'aeiou'))

def solve_04_P14():
	print(eval(input()))