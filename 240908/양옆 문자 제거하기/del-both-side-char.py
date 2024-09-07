text = input()

result = ''

for idx, c in enumerate(text):
    if idx != 1 and idx != len(text) - 2:
        result += c

print(result)