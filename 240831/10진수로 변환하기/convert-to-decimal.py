n = input()

n = n[-1::-1]

result = 0

for weight, value in enumerate(n):
    if value == '1':
        result += 2 ** (weight)

print(result)