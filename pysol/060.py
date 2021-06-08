N = int(input())
A = list(map(int, input().split()))

def LIS(L):
    from bisect import bisect_left
    ret = []
    seq = []
    for ai in L:
        pos = bisect_left(seq, ai)
        if len(seq) <= pos:
            seq.append(ai)
        else:
            seq[pos] = ai
        ret += [len(seq)]
    return ret

increase_seq = LIS(A)
decreace_seq = LIS(A[::-1])

ans = 0
for i in range(N):
    ans = max(ans, increase_seq[i] + decreace_seq[N-1-i] - 1)

print(ans)
