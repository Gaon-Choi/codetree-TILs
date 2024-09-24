N, M = map(int, input().split())

a = 0
a_t = 0
b = 0
b_t = 0

arr_a = []
arr_b = []

for _ in range(N):
    v, t = map(int, input().split())
    for _ in range(t):
        a_t += 1
        a += v
        arr_a.append(a)

for _ in range(M):
    v, t = map(int, input().split())
    for _ in range(t):
        b_t += 1
        b += v
        arr_b.append(b)

temp = []

for i in range(min(len(arr_a), len(arr_b))):
    winner = 1 if arr_a[i] > arr_b[i] else 2 if arr_a[i] == arr_b[i] else 3

    if temp and temp[-1] != winner:
        temp.append(winner)
    elif not temp:
        temp.append(winner)

print(len(temp))