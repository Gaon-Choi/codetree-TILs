text = list(input())

c = text[1]

for i in range(len(text)):
    if text[i] == c:
        text[i] = text[0]

print("".join(text))