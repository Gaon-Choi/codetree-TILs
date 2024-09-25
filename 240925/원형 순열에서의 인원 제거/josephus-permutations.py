N, K = map(int, input().split())

arr = list(range(1, N + 1))

pointer = 0

while arr:
    pointer += K

    if pointer > len(arr):
        pointer = pointer % len(arr)

        if pointer == 0:
            pointer += len(arr)

    pointer -= 1

    print(arr.pop(pointer), end=" ")