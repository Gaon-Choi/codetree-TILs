braces = input()

cnt = 0

for i in range(len(braces)):
    for j in range(i+1, len(braces)):
        if braces[i:i+2] == "((" and braces[j:j+2] == "))":
            cnt += 1

print(cnt)