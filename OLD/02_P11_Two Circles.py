x1, y1, r1, x2, y2, r2 = [float(x) for x in input().strip().split()]
diff = ((x1-x2)**2 + (y1-y2)**2)**0.5 - (r1+r2)
print(1 if diff == 0 else 2 if diff < 0 else 3)