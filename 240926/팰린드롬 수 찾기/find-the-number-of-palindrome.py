def is_palindrome(number: int):
    text = str(number)

    if text == text[-1::-1]:
        return True
    return False

X, Y = map(int, input().split())

cnt = 0

for num in range(X, Y + 1):
    if is_palindrome(num):
        cnt += 1

print(cnt)