a = list(input())

for i in range(len(a)):
    if a[i] == '0':
        a[i] = '1'
        break

a = ''.join(a)

result = 0

for i in range(-1, -(len(a) + 1), -1):
    result += 2 ** (-i - 1) * int(a[i])

print(result)