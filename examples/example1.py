nums = [6, 7, -2, 4, -4, 6, 12, 5]

# find max subarray

max_sum = float('-inf')
current_sum = 0
for i in range(len(nums)):
    current_sum += nums[i]
    if current_sum > max_sum:
        max_sum = current_sum
    if current_sum < 0:
        current_sum = 0

print(max_sum)