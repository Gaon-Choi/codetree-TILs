# Run-Length Encoding
## 간단한 비손실 압축 방식
## 연속해서 나온 문자와 연속해서 나온 개수로 나타내는 방식

result = ''

text = input()

prev = None
count = 1

for c in text:
    if prev is None:
        prev = c
        count = 1
    
    elif prev == c:
        count += 1
    else:
        result += str(prev) + str(count)
        count = 1
        prev = c

result += str(prev) + str(count)

print(len(result))
print(result)