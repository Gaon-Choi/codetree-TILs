word, c = input().split()

for i in range(len(word)):
    if word[i] == c:
        print(i)
        exit(0)

print("No")