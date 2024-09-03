N = int(input())

words = []

for _ in range(N):
    words.append(input())

total_size = 0
total_count = 0

c = input()

for word in words:
    if word[0] == c:
        total_count += 1
        total_size += len(word)

print(total_count, format(total_size / total_count, ".2f"))