n, k = map(int, input().split())

hashMap = dict()

for i in range(1, k):
    hashMap["{a}-{b}".format(a=i, b=k-i)] = 0

arr = list(map(int, input().split()))

for i in range(n):
    for j in range(i+1, n):
        if (str(arr[i]) + "-"+ str(arr[j])) in hashMap:
            hashMap[str(arr[i]) + "-"+ str(arr[j])] += 1

print(sum(hashMap.values()))