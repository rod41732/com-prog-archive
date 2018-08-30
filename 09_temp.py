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

# ---------------- LOOOL 4HEad -----------------
if sublime:
    __OMEGALUL__.close()
if tofile and sublime:
    __LUL3D___.close()
# ----------------------------------------------