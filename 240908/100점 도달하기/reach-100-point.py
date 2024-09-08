def get_grade(n: int):
    if n >= 90:
        return "A"
    elif n >= 80:
        return "B"
    elif n >= 70:
        return "C"
    elif n >= 60:
        return "D"
    else:
        return "F"

score = int(input())

for s in range(score, 100 + 1):
    print(get_grade(s), end=" ")