N, K = map(int, input().split())

if N == 0:
    exit(print(0))

def to_ten(num):
    ret = 0
    num_str = str(num)
    for s in num_str:
        ret += int(s)
        ret *= 8
    ret //= 8

    return ret


def nineth_adic(num):
    ret = ""
    while num:
        num, rem = num//9, num%9
        ret += str(rem)

    return ret[::-1]

def eight_to_five(num_st):
    num_st = num_st.replace("8", "5")
    return int(num_st)

for _ in range(K):
    N = to_ten(N)
    N = nineth_adic(N)
    N = eight_to_five(N)

print(N)
