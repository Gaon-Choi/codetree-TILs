from sortedcontainers import SortedDict

n = int(input())

dictionary = SortedDict()

for _ in range(n):
    word = input()
    if word in dictionary:
        dictionary[word] += 1
    else:
        dictionary[word] = 1

for k in dictionary:
    print(k, dictionary[k])