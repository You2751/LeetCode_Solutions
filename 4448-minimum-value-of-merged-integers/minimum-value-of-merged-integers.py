class Solution:
    def minMergedInteger(self, nums: list[int]) -> int:
        result = float('inf')
        for i in range(0, len(nums) - 1, 2):
            num = str(nums[i]) + str(nums[i + 1])
            result = min(result, int(num))
        return result