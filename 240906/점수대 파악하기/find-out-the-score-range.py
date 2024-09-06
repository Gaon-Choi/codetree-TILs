result = [0] * 11

arr = list(map(int, input().split()))

for elem in arr:
    if elem == 0:
        break
    if elem // 10 > 0:
        result[elem // 10] += 1

for i in range(len(result) - 1, 0, -1):
    print("{a} - {b}".format(a=i * 10, b = result[i]))