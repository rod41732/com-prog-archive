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
import random
import numpy as np 
import matplotlib.pyplot as plt
scores = np.array([random.randint(30, 95) for _ in range(20)])
rmin = [0, 50, 60, 70, 80]
rmax = [50, 60, 70, 80, 100]
print('SCORES\n',scores)
#base
# groups = [scores[(mn <= scores) & (scores < mx)] for mn, mx in zip(rmin, rmax)]
# avg = [np.mean(data) for data in groups]
# stddev = [np.std(data) for data in groups]
# drange = [np.max(data) - np.min(data) for data in groups]
# freq = [len(data) for data in groups]
# print(groups, avg, stddev, drange, freq, sep='\n')
# plt.bar(range(5), freq)
# plt.show()
x_val = np.arange(0, 5*np.pi, 0.05)
y_val = np.sin(x_val)
plt.plot(x_val, y_val)
plt.show()
# ---------------- LOOOL 4HEad -----------------
if sublime:
    __OMEGALUL__.close()
if tofile and sublime:
    __LUL3D___.close()
# ----------------------------------------------
