n = int(input())

is_five_multiple = 1 if n % 5 == 0 else 0
arr = [n]

e = n

while (is_five_multiple < 2):
    e = e + n
    if e % 5 == 0:
        is_five_multiple += 1
    arr.append(e)


for elem in arr:
    print(elem, end=" ")