def bmi(h, w):
    return 10000 * w / (h ** 2)

h, w = map(int, input().split())

result = bmi(h, w)
print(int(result))

if result >= 25:
    print("Obesity")