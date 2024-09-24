n = int(input())

arr = list(map(int, input().split()))

answer = dict()

for i in range(n):
    for j in range(i + 1, n):
        if (arr[i] + arr[j]) / 2 in answer:
            answer[(arr[i] + arr[j]) / 2] += 1
        else:
            answer[(arr[i] + arr[j]) / 2] = 1

print(max(answer.values()))