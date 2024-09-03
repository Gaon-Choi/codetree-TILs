def get_unique_alphabet_count(word):
    return len(set(list(word)))

text = input()

if get_unique_alphabet_count(text) >= 2:
    print("Yes")
else:
    print("No")