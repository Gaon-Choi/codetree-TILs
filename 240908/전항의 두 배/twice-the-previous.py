a1, a2 = map(int, input().split())

arr = [a1, a2]

for _ in range(8):
    arr.append(arr[-1] + arr[-2] * 2)

for elem in arr:
    print(elem, end=" ")