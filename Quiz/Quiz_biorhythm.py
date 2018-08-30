from math import pi, sin
bd, bm, by, d, m, y = [int(x) for x in input().strip().split()]
by -= 543
y -= 543
ans = 0
dim1 = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
diy1 = 365
dim2 = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
#x1 = x2 = 0
if (by%4 == 0 and by%100 != 0) or by%400 == 0:
  dim1[2] += 1
if (y%4 == 0 and y%100 != 0) or y%400 == 0:
  dim2[2] += 1
"""
for i in range(bm):
  x1 += dim1[i]
"""
# dates till 31 dec
ans += dim1[bm]-bd
bm += 1
while bm <= 12:
  ans += dim1[bm]
  bm += 1
# date from 31 dec  
for i in range(m):
  ans += dim2[i]
ans += d 
ans += (y-by-1)*365
print("%d %.2f %.2f %.2f"%(ans, sin(2*pi*ans/23), sin(2*pi*ans/28), sin(2*pi*ans/33)))