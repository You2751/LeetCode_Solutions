class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        result = left = 0
        for right, num in enumerate(nums):
            while(left < right and nums[right] - k > nums[left] + k):
                left += 1
            result = max(result, right - left + 1)
        return result