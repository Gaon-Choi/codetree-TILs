n, k, T = input().split()

n = int(n); k = int(k)

words = []

for _ in range(n):
    word = input()
    if word[0:len(T)] == T:
        words.append(word)

words.sort()

print(words[k-1])