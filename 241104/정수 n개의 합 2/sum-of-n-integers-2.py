n, k = map(int, input().split())

arr = list(map(int, input().split()))

# 부분합 배열 생성
sum_arr = [arr[0]]

for i in range(1, n):
    sum_arr.append(sum_arr[-1] + arr[i])

answer = sum_arr[k - 1]

for i in range(n - k):
    answer = max(answer, sum_arr[i + k] - sum_arr[i])

print(answer)