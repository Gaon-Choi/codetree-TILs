arr = []

while(True):
    age = int(input())

    if not(20 <= age and age <= 29):
        break

    arr.append(age)

print(format(round(sum(arr) / len(arr), 2), ".2f"))