text = input()

dictionary = dict()

for c in text:
    if c in dictionary:
        dictionary[c] += 1
    else:
        dictionary[c] = 1

answer = 'None'

for elem in dictionary:
    if dictionary[elem] == 1:
        answer = elem
        break

print(answer)