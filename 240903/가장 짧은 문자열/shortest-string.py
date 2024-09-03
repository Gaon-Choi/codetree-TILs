length = []

for _ in range(3):
    length.append(len(input()))

print(max(length) - min(length))