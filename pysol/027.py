N = int(input())

se = set()
for i in range(N):
    s = input()
    if s in se:
        continue
    se.add(s)
    print(i+1)
