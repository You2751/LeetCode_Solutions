class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        def is_increasing(nums):
            for i in range(1, len(nums)):
                if(nums[i - 1] > nums[i]):
                    return False
            return True
        def is_decreasing(nums):
            for i in range(1, len(nums)):
                if nums[i - 1] < nums[i]:
                    return False
            return True
        return is_increasing(nums) or is_decreasing(nums)