n = int(input())

zenga = []

for _ in range(n):
    zenga.append(int(input()))

s1, e1 = map(int, input().split())
zenga = zenga[:s1-1] + zenga[e1:]

s2, e2 = map(int, input().split())
zenga = zenga[:s2-1] + zenga[e2:]

print(len(zenga))

for elem in zenga:
    print(elem)