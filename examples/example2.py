nums = [6, 7, -2, 4, -4, 6, 12, 5]

# Find a pair of numbers that sum to n.

def find_pair(nums, n):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == n:
                return nums[i], nums[j]
    return None