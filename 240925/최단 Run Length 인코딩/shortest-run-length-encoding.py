def run_length_encoding(text):
    prev = text[0]
    count = 0

    result = ""

    for c in text:
        if prev == c:
            count += 1
        else:
            result += prev + str(count)
            prev = c
            count = 1

    if count > 0:
        result += prev + str(count)

    return result

text = input()
temp_answer = []

for _ in range(len(text)):
    text = text[1:] + text[0]
    temp_answer.append(len(run_length_encoding(text)))

print(min(temp_answer))