a, b = map(int, input().split())

n = input()

n = n[-1::-1]

result = 0
for weight, value in enumerate(n):
    result += (a ** weight) * int(value)

result2 = []

while(True):
    if result < b:
        result2.append(str(result))
        break

    result2.append(str(result % b))
    result = result // b

result2.reverse()

print(''.join(result2))