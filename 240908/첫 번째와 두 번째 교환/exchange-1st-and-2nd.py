text = list(input())

first = text[0]; second = text[1]

for i in range(len(text)):
    if text[i] == first:
        text[i] = second
    elif text[i] == second:
        text[i] = first

print("".join(text))