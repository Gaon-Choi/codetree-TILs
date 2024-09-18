alphabet = list(range(ord('a'), ord('z') + 26))

idx = ord(input())

print(chr(alphabet[(idx + 1 - ord('a')) % 26]))