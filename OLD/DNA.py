dna = input().strip().upper()
cmd = input().strip()
chars = 'ATGC'
valid = 1
for char in dna:
    if char not in chars:
        valid = 0
        break
if valid == 0:
    print("Invalid DNA")
else:
    if cmd == 'R':
        out = ''
        for char in dna[::-1]:
            if char == 'A':
                out += 'T'
            if char == 'T':
                out += 'A'
            if char == 'G':
                out += 'C'
            if char == 'C':
                out += 'G'
        print(out)
    if cmd == 'F':
        ca = ct = cg = cc = 0
        for char in dna:
            if char == 'A':
                ca += 1
            if char == 'T':
                ct += 1
            if char == 'G':
                cg += 1
            if char == 'C':
                cc += 1
        print('A=%d, T=%d, G=%d, C=%d'%(ca, ct, cg, cc))
    if cmd == 'D':
        key = input().strip().upper()
        cnt = 0
        idx = 0
        while (idx != -1):
            idx = dna.find(key, idx)
            if idx != 0:
                idx += 1
                cnt += 1
        print(cnt)