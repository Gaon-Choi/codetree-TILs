hospital = {
    "A": 0,
    "B": 0,
    "C": 0,
    "D": 0
}

for _ in range(3):
    is_flu, temperature = input().split()
    temperature = int(temperature)

    if is_flu == "Y" and temperature >= 37:
        hospital["A"] += 1
    elif is_flu == "N" and temperature >= 37:
        hospital["B"] += 1
    elif is_flu == "Y" and temperature < 37:
        hospital["C"] += 1
    else:
        hospital["D"] += 1

print(hospital["A"], hospital["B"], hospital["C"], hospital["D"], end=" ")

if hospital["A"] >= 2:
    print("E")