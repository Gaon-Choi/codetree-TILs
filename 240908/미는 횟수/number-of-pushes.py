def rotate_right(text: str):
    return text[-1] + text[:-1]

A = input()
B = input()

num = 0

while(True):
    A = rotate_right(A)
    num += 1

    if A == B:
        break

    if num == len(A):
        print(-1)
        exit(0)

print(num)