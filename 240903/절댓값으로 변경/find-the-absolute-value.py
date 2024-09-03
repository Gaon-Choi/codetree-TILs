def abs_all(aList):
    for i in range(len(aList)):
        aList[i] = abs(aList[i])
    

N = int(input())

arr = list(map(int, input().split()))
abs_all(arr)

for elem in arr:
    print(elem, end=" ")