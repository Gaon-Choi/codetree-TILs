n, t = map(int, input().split())

convey_1 = list(map(int, input().split()))
convey_2 = list(map(int, input().split()))
convey_3 = list(map(int, input().split()))

for _ in range(t):
    pop_1 = convey_1.pop(n - 1)
    pop_2 = convey_2.pop(n - 1)
    pop_3 = convey_3.pop(n - 1)

    convey_2.insert(0, pop_1)
    convey_3.insert(0, pop_2)
    convey_1.insert(0, pop_3)

for elem in convey_1:
    print(elem, end=" ")
print()
for elem in convey_2:
    print(elem, end=" ")
print()
for elem in convey_3:
    print(elem, end=" ")