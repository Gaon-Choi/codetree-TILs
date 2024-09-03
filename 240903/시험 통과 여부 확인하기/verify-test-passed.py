score = int(input())

if score >= 80:
    print("pass")
else:
    print("{remain} more score".format(remain=(80-score)))