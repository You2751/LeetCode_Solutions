class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        valid = [False] * n
        best = 0
        for left, num in enumerate(nums):
            if(num > best):
                valid[left] = True
                best = nums[left]
        best = 0
        for right in range(n - 1, -1, -1):
            if(nums[right] > best):
                valid[right] = True
                best = nums[right]
        return [val for val, check in zip(nums, valid) if check]