class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        diff = abs(nums[-1] - nums[0])
        for idx in range(1, len(nums)):
            diff = max(diff, abs(nums[idx] - nums[idx - 1]))
        return diff