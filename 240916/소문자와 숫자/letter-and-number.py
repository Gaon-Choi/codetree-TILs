text = input()
answer = ""

for c in text:
    if c.isalpha():
        answer += c.lower()
    elif c.isdigit():
        answer += c

print(answer)