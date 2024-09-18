arr = list(map(int, input().split()))

answer = []

for elem in arr:
    answer.append(chr(elem))

for elem in answer:
    print(elem, end=" ")