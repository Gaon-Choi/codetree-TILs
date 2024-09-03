words = []

for _ in range(10):
    words.append(input())

c = input()

isEmpty = True

for elem in words:
    if elem[-1] == c:
        print(elem)
        isEmpty = False

if isEmpty:
    print("None")