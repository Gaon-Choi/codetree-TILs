result = []

for _ in range(3):
    is_flu, temp = input().split()
    temp = int(temp)

    if is_flu == "Y":
        if temp >= 37:
            result.append("A")
        else:
            result.append("C")
    else:
        if temp >= 37:
            result.append("B")
        else:
            result.append("D")

if result.count("A") >= 2:
    print("E")
else:
    print("N")