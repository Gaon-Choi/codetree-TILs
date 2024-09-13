from sortedcontainers import SortedDict

n = int(input())

words = SortedDict()

for _ in range(n):
    word = input()

    if word in words:
        words[word] += 1
    else:
        words[word] = 1

total = sum(words.values())

for k in words:
    print(k, format(round(100 * words[k] / total, 4), ".4f"))