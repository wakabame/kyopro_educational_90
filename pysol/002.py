N = int(input())


def valid_parenthesis(parenthesis_string):
    cnt = 0
    for i in range(len(parenthesis_string)):
        if parenthesis_string[i] == "(":
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            return False
    if cnt != 0:
        return False
    return True


ans_list = []
for i in range(1 << N):
    parenthesis_string = ""
    for k in range(N):
        if i & (1 << k):
            parenthesis_string = ")" + parenthesis_string
        else:
            parenthesis_string = "(" + parenthesis_string

    if valid_parenthesis(parenthesis_string):
        ans_list += [parenthesis_string]

for ans in ans_list:
    print(ans)
