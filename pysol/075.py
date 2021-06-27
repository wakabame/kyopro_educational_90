N = int(input())

prime_count = 0

curr = 2
while curr * curr <= N:
    if N%curr == 0:
        prime_count += 1
        N //= curr
    else:
        curr += 1
if N > 1:
    prime_count += 1


ans = 0
power = 1
while True:
    if prime_count <= power:
        exit(print(ans))
    ans += 1
    power *= 2
