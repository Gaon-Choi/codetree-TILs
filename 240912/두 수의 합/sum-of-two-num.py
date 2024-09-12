n, k = map(int, input().split())
arr = list(map(int, input().split()))

for elem in arr:
    if elem in hashMap:
        hashMap[elem] += 1
    else:
        hashMap[elem] = 1

hashMap = dict()



print(sum(hashMap.values()))