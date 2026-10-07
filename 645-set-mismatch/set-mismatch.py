class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        dub = missing = None
        for num in nums:
            idx = abs(num) - 1
            if(nums[idx] < 0):
                dub = abs(num)
            else:
                nums[idx] = -nums[idx]
        for idx, num in enumerate(nums):
            if(num > 0):
                missing = idx + 1
                break
        return [dub, missing]