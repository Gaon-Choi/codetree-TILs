from sortedcontainers import SortedDict

n = int(input())

characterLocation = SortedDict()

arr = list(map(int, input().split()))

for idx, elem in enumerate(arr):
    if elem not in characterLocation:
        characterLocation[elem] = idx + 1

for k in characterLocation:
    print(k, characterLocation[k])