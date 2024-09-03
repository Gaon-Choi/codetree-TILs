text = input()

c = input()

cnt = 0
for elem in text:
    if elem == c:
        cnt += 1

print(cnt)