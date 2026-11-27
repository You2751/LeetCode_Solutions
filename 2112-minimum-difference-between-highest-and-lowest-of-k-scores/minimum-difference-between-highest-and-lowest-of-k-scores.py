class Solution:
    def minimumDifference(self, nums: list[int], k: int) -> int:
        nums.sort()
        result = float('inf')
        left, right = 0, k - 1
        while(right < len(nums)):
            diff = nums[right] - nums[left]
            result = min(result, diff)
            left += 1
            right += 1
        return result