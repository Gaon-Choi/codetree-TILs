N = int(input())

count_first_a = 0
size_total = 0

for _ in range(N):
    text = input()
    if text[0] == "a":
        count_first_a += 1
    size_total += len(text)

print(size_total, count_first_a)