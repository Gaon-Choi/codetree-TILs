t1, t2 = input().split()

if len(t1) > len(t2):
    print(t1, len(t1))
elif len(t1) < len(t2):
    print(t2, len(t2))
else:
    print("same")