N = int(input())

string_arr = ''.join(input().split())

for i in range(len(string_arr)):
    print(string_arr[i], end="")
    if i % 5 == 4:
        print()