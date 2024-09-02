N = int(input())

hashmap = dict()

for _ in range(N):
    elem = input()

    if elem in hashmap:
        hashmap[elem] += 1
    else:
        hashmap[elem] = 1

max_key = None
max_count = -1

print(max(hashmap.values()))