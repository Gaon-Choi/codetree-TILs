word = input()
queries = input()

for q in queries:
    if q == "L":
        word = word[1:] + word[0]
    else:
        word = word[-1] + word[:-1]

print(word)