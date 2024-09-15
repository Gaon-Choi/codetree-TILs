text = input()
answer = ""

for c in text:
    if c.islower():
        answer += c.upper()
    else:
        answer += c.lower()

print(answer)