def is_interesting(n: int):
    number_str = str(n)
    digits = list(set(list(str(n))))
    if len(digits) == 2:
        if number_str.count(digits[0]) == 1 or number_str.count(digits[1]) == 1:
            return True
        else:
            return False
    return False

X, Y = map(int, input().split())

result = 0

for num in range(X, Y + 1):
    if is_interesting(num):
        result += 1

print(result)