N = int(input())
A = list(map(int ,input().split()))
if sum(A)%10:
  exit(print("No"))

ans = sum(A)//10
A += A
st, en = 0, 0
curr = 0
while st < 2 * N:
  if curr == ans:
    exit(print("Yes"))
  if st == en:
    curr += A[en]
    en += 1
  elif en == 2*N:
    curr -= A[st]
    st += 1
  elif curr < ans:
    curr += A[en]
    en += 1
  elif curr > ans:
    curr -= A[st]
    st += 1
print("No")
