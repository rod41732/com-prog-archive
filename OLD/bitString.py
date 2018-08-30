n = int(input())
bits = input()
k = len(bits)
ans = 0
for offset in range(0, n-k+1):
    ans += 2**(n-k)
    for i in range(1, offset+1):
        i = min(k, i)
        if bits[0:k-i] == bits[i:k]:
            ans -= 2**(n-k-i)
print(ans)


