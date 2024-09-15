text = input()
answer = ''

for c in text:
    if c.isalpha():
        answer += c.upper()

print(answer)