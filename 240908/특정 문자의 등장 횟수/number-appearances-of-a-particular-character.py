cnt_1 = 0
cnt_2 = 0

word_1 = "ee"
word_2 = "eb"

text = input()

for i in range(len(text)):
    if i + len(word_1) - 1 < len(text):
        if text[i:i+len(word_1)] == word_1:
            cnt_1 += 1
    if i + len(word_2) - 1 < len(text):
        if text[i:i+len(word_2)] == word_2:
            cnt_2 += 1

print(cnt_1, cnt_2)