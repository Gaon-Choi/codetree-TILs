braces = input()

result = 0

for i in range(len(braces)):
    for j in range(i, len(braces)):
        if braces[i] == '(' and braces[j] == ')':
            result += 1

print(result)