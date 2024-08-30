even_sum = 0
three_list = []

nums = list(map(int, input().split()))

for i in range(len(nums)):
    if (i+1) % 2 == 0:
        even_sum += nums[i]

    if (i+1) % 3 == 0:
        three_list.append(nums[i])

print(even_sum, round(sum(three_list) / len(three_list), 1))