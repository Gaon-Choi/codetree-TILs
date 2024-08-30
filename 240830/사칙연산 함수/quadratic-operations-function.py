text = input()

a, o, c = text.split()

a = int(a); c = int(c)

result = None

if o =="+":
    result = a + c
elif o =="-":
    result = a - c
elif o =="/":
    result = a // c
elif o =="*":
    result = a * c
else:
    print("False")
    exit(0)

print("{text} = {ans}".format(text=text, ans=result))