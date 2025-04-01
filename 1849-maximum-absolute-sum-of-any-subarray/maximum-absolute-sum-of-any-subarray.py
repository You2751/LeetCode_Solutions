class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_sum = min_sum = result = 0
        for num in nums:
            max_sum = max(max_sum + num, 0)
            min_sum = min(min_sum + num, 0)
            result = max(result, max_sum, abs(min_sum))
        return result