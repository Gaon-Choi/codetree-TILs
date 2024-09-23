n, m = map(int, input().split())

linked_list = []
pointer = n

for c in input():
    linked_list.append(c)

for _ in range(m):
    query = input().split()

    if query[0] == "L":
        if 0 < pointer and pointer <= len(linked_list):
            pointer -= 1
    
    elif query[0] == "R":
        if 0 <= pointer and pointer < len(linked_list):
            pointer += 1

    elif query[0] == "D":
        if pointer == len(linked_list):
            continue
        else:
            linked_list.pop(pointer)

    else:
        linked_list.insert(pointer, query[1])
        pointer += 1

for elem in linked_list:
    print(elem, end="")