N, K = map(int, input().split())

arr = [0] * 101

for _ in range(N):
    temp = list(map(int, input().split()))
    arr[temp[1]] += temp[0]

temp_arr = []

for i in range(101):
    temp_arr.append(sum(arr[max(0, i-K):min(100, i+K) + 1]))

print(max(temp_arr))