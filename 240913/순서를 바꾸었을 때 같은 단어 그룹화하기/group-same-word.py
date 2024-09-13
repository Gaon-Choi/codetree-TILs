n = int(input())

words = dict()

for _ in range(n):
    word = ''.join(sorted(list(input())))
    if word in words:
        words[word] += 1
    else:
        words[word] = 1

print(max(words.values()))