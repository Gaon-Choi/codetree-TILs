text = input()

answer = 0

for c in text:
    if c.isdigit():
        answer += int(c)

print(answer)