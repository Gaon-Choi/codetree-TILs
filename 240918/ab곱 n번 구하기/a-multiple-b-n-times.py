def multiply_range(a, b):
    result = 1
    
    temp = a

    while (temp <= b):
        result *= temp
        temp += 1

    return result

n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    print(multiply_range(a, b))