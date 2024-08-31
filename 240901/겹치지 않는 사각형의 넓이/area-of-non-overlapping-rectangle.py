size = 2001
offset = size // 2

a_x1, a_y1, a_x2, a_y2 = map(int, input().split())

b_x1, b_y1, b_x2, b_y2 = map(int, input().split())

m_x1, m_y1, m_x2, m_y2 = map(int, input().split())

matrix = [[0] * size for _ in range(size)]

for i in range(a_x1, a_x2):
    for j in range(a_y1, a_y2):
        matrix[i + offset][j + offset] = 1

for i in range(b_x1, b_x2):
    for j in range(b_y1, b_y2):
        matrix[i + offset][j + offset] = 1

for i in range(m_x1, m_x2):
    for j in range(m_y1, m_y2):
        matrix[i + offset][j + offset] = 0

result = 0

for i in range(size):
    for j in range(size):
        result += matrix[i][j]

print(result)