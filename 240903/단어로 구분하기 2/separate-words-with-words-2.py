text = input().split()

for idx, value in enumerate(text):
    if idx % 2 == 0:
        print(value)