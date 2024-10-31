def is_bombable(arr, idx):
    start = max(0, idx - K)
    end = min(N-1, idx + K)

    if arr[idx] in arr[start:end+1]:
        return True
    return False

bomb_list = dict()

N, K = map(int, input().split())

arr = []

for _ in range(N):
    arr.append(int(input()))

for idx in range(N):
    if is_bombable(arr, idx):
        if arr[idx] in bomb_list:
            bomb_list[arr[idx]] += 1
        else:
            bomb_list[arr[idx]] = 1

bomb_list = sorted(bomb_list.items(), key=lambda x: (-x[1], -x[0]))

if len(bomb_list) > 0:
    print(bomb_list[0][0])
else:
    print(0)