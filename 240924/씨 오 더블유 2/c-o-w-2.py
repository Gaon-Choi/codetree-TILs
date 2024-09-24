N = int(input())
text = input()

cnt = 0

for i in range(len(text) - 2):
    if text[i] == "C":
        text_1 = text[i+1:]

        for j in range(len(text_1)):
            if text_1[j] == "O":
                text_2 = text[j+1:]

                for k in range(len(text_2)):
                    if text_2[k] == "W":
                        cnt += 1

print(cnt)