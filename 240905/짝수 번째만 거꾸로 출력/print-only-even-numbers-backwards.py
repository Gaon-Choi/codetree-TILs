text = input()

result = ''

for i in range(len(text)):
    if i % 2 == 1:
        result += text[i]

print(result[-1::-1])