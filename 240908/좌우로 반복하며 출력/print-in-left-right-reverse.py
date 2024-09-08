n = int(input())

text = ''.join(map(str, range(1, n + 1)))

for _ in range(n):
    print(text)
    text = text[-1::-1]