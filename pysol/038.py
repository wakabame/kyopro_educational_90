from math import gcd

a, b = map(int, input().split())
gc = gcd(a, b)
lc = (a * b) // gc

if lc > 10 ** 18:
    print("Large")
else:
    print(gc)
