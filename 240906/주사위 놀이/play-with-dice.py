arr = list(map(int, input().split()))

result = [0] * (6 + 1)

for elem in arr:
    result[elem] += 1

for i in range(1, len(result)):
    print("{i} - {result}".format(i=i, result=result[i]))