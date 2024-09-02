N = int(input())

arr = []

for i in range(N, 0, -1):
    arr.append(i)

for i in range(2, N + 1):
    arr.append(i)

for elem in arr:
    print("* " * elem)