N = int(input())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))

ans = sum([abs(a - b) for a, b in zip(A, B)])
print(ans)
