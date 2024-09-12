attendance_list = {
    1: "John",
    2: "Tom",
    3: "Paul",
    4: "Sam"
}

while(True):
    n = int(input())

    if n in attendance_list:
        print(attendance_list[n])
    else:
        print("Vacancy")
        break