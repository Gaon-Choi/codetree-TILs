n = int(input())

min_arr = []
max_arr = []

for _ in range(n):
    x, y = map(int, input().split())
    min_arr.append(x)
    max_arr.append(y)

answer = -1

for x in range(1, 15):
    num = x

    is_flag = False

    for i in range(n):
        num *= 2
        if min_arr[i] <= num and num <= max_arr[i]:
            continue
        else:
            is_flag = True
            break

    if not is_flag:
        answer = x
        break

print(answer)