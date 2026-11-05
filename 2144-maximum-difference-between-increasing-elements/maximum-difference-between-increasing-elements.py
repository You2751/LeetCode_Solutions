class Solution:
    def maximumDifference(self, nums: list[int]) -> int:
        result = float('-inf')
        min_val = nums[0]
        for idx in range(1, len(nums)):
            if(nums[idx] > min_val):
                result = max(result, nums[idx] - min_val)
            else:
                min_val = nums[idx]
        if(result == float('-inf')):
            return -1
        return result