n, t = map(int, input().split())

convey1 = list(map(int, input().split()))
convey2 = list(map(int, input().split()))

for _ in range(t):
    end_1 = convey1.pop(n-1)
    end_2 = convey2.pop(n-1)

    convey2.insert(0, end_1)
    convey1.insert(0, end_2)

for elem in convey1:
    print(elem, end=" ")
print()
for elem in convey2:
    print(elem, end=" ")