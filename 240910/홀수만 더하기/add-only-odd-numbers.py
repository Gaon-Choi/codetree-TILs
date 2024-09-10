n = int(input())

arr = []

for _ in range(n):
    elem = int(input())
    if elem % 2 == 1 and elem % 3 == 0:
        arr.append(elem)

print(sum(arr))