n = int(input())

arr = list(map(int, input().split()))

answer = dict()

for i in range(n):
    for j in range(i, n):
        if (arr[i] + arr[j]) in answer:
            answer[(arr[i] + arr[j])] += 1
        else:
            answer[(arr[i] + arr[j])] = 1

print(max(answer.values()))