from math import ceil
dist = ceil(float(input().strip()))
ans = 35-5.5
ans += 5.5*dist + max(0, dist-10) + max(0, dist-20)*1 + max(0, dist-40)*0.5 + max(0, dist-60) + max(0, dist-80)*1.5
print(ans)



