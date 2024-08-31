N , K = map(int, input().split())

blocks_list = [0] * N

for _ in range(K):
    start, end = map(int, input().split())

    for i in range(start-1, end):
        blocks_list[i] += 1

print(max(blocks_list))