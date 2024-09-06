result = [0] * (9 + 1)

arr = list(map(int, input().split()))

for elem in arr:
    if elem == 0:
        break
    result[elem // 10] += 1

for i in range(1, len(result)):
    print("{i} - {result}".format(i=i, result=result[i]))