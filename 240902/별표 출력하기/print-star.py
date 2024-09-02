N = int(input())

arr = []

for i in range(1, N + 1):
    arr.append(i)

for i in range(N-1, 0, -1):
    arr.append(i)

for elem in arr:
    print("* " * elem)