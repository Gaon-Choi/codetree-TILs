word, q = input().split()
q = int(q)

for _ in range(q):
    query = int(input())

    if query == 1:
        word = word[1:] + word[0]
    elif query == 2:
        word = word[-1] + word[:-1]
    elif query == 3:
        word = word[-1::-1]

    print(word)