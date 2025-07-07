def contains(nums, tar):
    def helper(i):
        if i == len(nums):
            return False
        return nums[i] == tar or helper(i+1)
    return helper(0)

print(contains([4, 1, 6, 8], 6))
print(contains([4, 1, 6, 8], 10))
