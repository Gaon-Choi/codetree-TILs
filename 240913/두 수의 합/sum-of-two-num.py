n, k = map(int, input().split())
arr = list(map(int, input().split()))

hashMap = dict()



for elem in arr:
    if elem in hashMap:
        hashMap[elem] += 1
    else:
        hashMap[elem] = 1

# arr = list(set(arr))

result = 0

for elem in arr:
    complement = k - elem
    # 원소가 중복될 수 있으므로 탐색 시마다 개수를 -1 해줘야함
    hashMap[elem] -= 1

    if complement in hashMap:
        result += hashMap[complement]

print(result)