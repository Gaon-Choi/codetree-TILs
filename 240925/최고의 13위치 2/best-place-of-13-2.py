def is_intersect(a1, b1, a2, b2):
    B = set([b1, b1 + 1, b1 + 2, b2, b2 + 1, b2 + 2])

    if a1 == a2 and len(B) != 6:
        return True
    else:
        return False

N = int(input())

matrix = []

for _ in range(N):
    matrix.append(list(map(int, input().split())))

cost = []

for a1 in range(N):
    for b1 in range(N):
        for a2 in range(N):
            for b2 in range(N):
                if not is_intersect(a1, b1, a2, b2) and b1 + 2 < N and b2 + 2 < N:
                    cost.append(matrix[a1][b1] + matrix[a1][b1 + 1] + matrix[a1][b1 + 2] + matrix[a2][b2] + matrix[a2][b2 + 1] + matrix[a2][b2 + 2])

print(max(cost))