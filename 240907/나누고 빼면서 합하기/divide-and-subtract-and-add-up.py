n, m = map(int, input().split())

arr = list(map(int, input().split()))

result = 0

while (m >= 1):
    # print(m, arr[m-1])

    result += arr[m - 1]

    if m % 2 == 1:
        m -= 1
    else:
        m = m // 2

print(result)