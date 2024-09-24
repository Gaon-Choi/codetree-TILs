def is_takable(temp_list):
    a1 = temp_list.count(1)
    a2 = temp_list.count(-1)

    if (a2 == 0 and a1 > 0) or (a1 == 0 and a2 > 0) or (a1 == a2 and a1 > 0 and a2 > 0):
        return True

    return False

size = 100

N = int(input())

arr = [0] * (size + 1)

for _ in range(N):
    location, alphabet = input().split()
    location = int(location)
    arr[location] = 1 if alphabet == "G" else -1

max_width = 0

for i in range(size + 1):
    for j in range(i, size + 1):
        picture_size = j - i

        if arr[i] != 0 and arr[j] != 0 and is_takable(arr[i:j + 1]):
            max_width = max(max_width, picture_size)

print(max_width)