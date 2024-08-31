N = int(input())

result = []

while(True):
    if N < 2:
        result.append(str(N))
        break

    result.append(str(N % 2))
    N = N // 2

result.reverse()

print(''.join(result))