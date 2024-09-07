text = input()

for _ in range(len(text) - 1):
    idx = int(input())
    if idx >= len(text):
        text = text[0:len(text) - 1]
    else:
        text = text[0:idx] + text[idx + 1:]
    print(text)