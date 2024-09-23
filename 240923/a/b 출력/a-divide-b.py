a, b = map(int, input().split())

arr = []

for _ in range(21):
    arr.append(str(a // b))
    
    a = a % b
    a *= 10

print(arr[0] + "." + "".join(arr[1:]))