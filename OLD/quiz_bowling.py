text = input().strip()
target = int(input())
numer = [0]*len(text)
framescore = [0]*10
now = 0
cnter = 0
for i in range(len(text)):
	if text[i] == 'X':
		numer[i] = 10
	elif text[i] == '/':
		numer[i] = 10-numer[i-1] # or int(text[i-1])
	else:
		numer[i] = int(text[i])
for i in range(len(numer)):
	if now == 9: #last frame, just add all numbers
		framescore[now] += numer[i]
	elif numer[i] == 10: #stike -> next frame
		framescore[now] = numer[i]+numer[i+1]+numer[i+2]
		cnter = 0
		now += 1
	else: # normal
		framescore[now] += numer[i]
		cnter += 1
		if cnter == 2: #2nd ball
			if text[i] == '/': #spare
				framescore[now] += numer[i+1]
			cnter = 0
			now += 1
if target in range(1, 11):
    print(framescore[target-1])
else:
    _sum = 0
    for num in framescore:
        _sum += num
    print(_sum)

