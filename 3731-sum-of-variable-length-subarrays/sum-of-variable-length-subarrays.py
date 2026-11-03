class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        result = 0
        for idx, num in enumerate(nums):
            start = max(0, idx - num)
            result += sum(nums[start: idx + 1])
        return result