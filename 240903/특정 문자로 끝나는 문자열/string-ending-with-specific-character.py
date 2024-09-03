words = []

for _ in range(10):
    words.append(input())

c = input()

for elem in words:
    if elem[-1] == c:
        print(elem)