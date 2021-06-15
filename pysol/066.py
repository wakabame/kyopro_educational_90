N = int(input())
LR = [list(map(int, input().split())) for _ in range(N)]

def calc_expect_by_two(LR1, LR2):
    l1, r1 = LR1
    l2, r2 = LR2

    bunshi = 0
    bunbo = 0
    for i in range(1, 101):
        for j in range(1, 101):
            if l1 <= i <= r1 and l2 <= j <= r2:
                bunbo += 1
                if i < j:
                    bunshi += 1

    return bunshi/bunbo

ans = 0

for i in range(N):
    for j in range(i):
        ans += calc_expect_by_two(LR[i], LR[j])

print(ans)
