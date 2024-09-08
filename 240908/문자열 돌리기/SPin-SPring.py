text = input()

print(text)

for _ in range(len(text)):
    text = text[-1] + text[:-1]
    print(text)