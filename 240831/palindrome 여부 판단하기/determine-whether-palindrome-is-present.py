def is_palindrome(text):
    flip_str = ''
    for i in range(1, len(text) + 1):
        flip_str += text[-i]

    return flip_str == text

test = input()

if is_palindrome(test):
    print("Yes")
else:
    print("No")