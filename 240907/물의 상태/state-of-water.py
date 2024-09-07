temperature = int(input())

if temperature < 0:
    print("ice")
elif temperature < 100:
    print("water")
else:
    print("vapor")