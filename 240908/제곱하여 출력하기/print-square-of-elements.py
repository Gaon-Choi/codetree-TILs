n = int(input())
arr = list(map(int, input().split()))

result = [elem ** 2 for elem in arr]

for elem in result:
    print(elem, end=" ")