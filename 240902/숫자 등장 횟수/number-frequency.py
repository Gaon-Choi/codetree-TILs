n, m = map(int, input().split())

hashmap = dict()
result = []

arr = list(map(int, input().split()))

for elem in arr:
    if elem in hashmap:
        hashmap[elem] += 1
    else:
        hashmap[elem] = 1

query = list(map(int, input().split()))
for q in query:
    if q in hashmap:
        result.append(hashmap[q])
    else:
        result.append(0)

for elem in result:
    print(elem, end=" ")