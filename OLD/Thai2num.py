num = {'soon':0, 'nueng':1, 'song':2, 'sam':3, 'see':4, 'ha':5, 'hok':6,
     'jed':7, 'pad':8, 'kao':9, 'yee':2, 'sip':10, 'roey':100, 'pun':1000,
       'muen':10000, 'saen':100000, 'larn':1000000, 'ed':1, 'lop':-1, 'jood':-2}
arr = input().split('-')
# print(arr)
arr = [num[i] for i in arr]
# print(arr)
ptr = 0
now = 0
ans = 0
numofdec = 0
strans = ""
flag = 1
isDec = 0
while ptr < len(arr): #convert to dec
    x = arr[ptr]
    if x == -2: # jood
        ptr += 1 # so next loop we start at numbe
        isDec = 1
        break
    if x == -1: # lop
        flag = -1
    elif x > 0 and x%10 == 0: # 10^n
        if x == 1000000:
            ans += now
            ans *= x
            now = 0
        else:
            now = x if now == 0 else now*x
    else: # 1...9
        ans += now
        now = x
    ptr += 1
ans += now # dec converted

if flag == -1:
    strans += '-'

n = len(str(ans))
offset = n%3
for i in range(n): # add comma
    if (i-offset)%3 == 0 and i > 0:
        strans += ','
    strans += str(ans)[i]

if isDec: # dot
    strans += '.'

while ptr < len(arr):
    strans += str(arr[ptr])
    ptr += 1
print(strans)


