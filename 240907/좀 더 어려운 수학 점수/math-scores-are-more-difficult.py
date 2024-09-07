a_mat, a_eng = map(int, input().split())
b_mat, b_eng = map(int, input().split())

if a_mat > b_mat:
    print("A")
elif a_mat < b_mat:
    print("B")
else:
    print("A" if a_eng > b_eng else "B")