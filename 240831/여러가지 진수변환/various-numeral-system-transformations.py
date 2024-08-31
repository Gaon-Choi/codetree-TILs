N, B = map(int, input().split())

result = []

while (True):
    if N < B:
        result.append(str(N))
        break

    result.append(str(N % B))
    N = N // B

result.reverse()

print(''.join(result))