N = int(input())

avg = sum(list(map(float, input().split()))) / 4

print(format(avg, ".1f"))

if avg >= 4.0:
    print("Perfect")
elif avg >= 3.0:
    print("Good")
else:
    print("Poor")