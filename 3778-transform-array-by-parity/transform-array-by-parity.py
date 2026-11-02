class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        for idx, num in enumerate(nums):
            if(num % 2):
                nums[idx] = 1
            else:
                nums[idx] = 0
        return sorted(nums)