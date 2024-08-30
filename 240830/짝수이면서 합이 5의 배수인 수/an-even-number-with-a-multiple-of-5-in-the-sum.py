n = int(input())

if n % 2 == 0 and sum(list(map(int, list(str(n))))) % 5 == 0:
    print("Yes")
else:
    print("No")