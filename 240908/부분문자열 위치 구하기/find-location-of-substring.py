text = input()
search = input()

for i in range(len(text)):
    if i + len(search) - 1 < len(text):
        if text[i:i+len(search)] == search:
            print(i)
            exit(0)

print(-1)