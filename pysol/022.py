import math

A, B, C = map(int, input().split())

gc = math.gcd(math.gcd(A, B), C)

ans = (A + B + C) // gc - 3

print(ans)
