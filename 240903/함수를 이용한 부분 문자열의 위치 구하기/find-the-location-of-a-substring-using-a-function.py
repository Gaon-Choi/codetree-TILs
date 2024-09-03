word = input()
search = input()

def search_word(word, search):
    for i in range(len(word) - len(search) + 1):
        if word[i:i+len(search)] == search:
            return i
    return -1

print(search_word(word, search))