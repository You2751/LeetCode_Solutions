class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        length = len(nums)
        result = total = left = 0
        for right, num in enumerate(nums):
            total += num
            while(left <= right and total * (right - left + 1) >= k):
                total -= nums[left]
                left += 1
            result += right - left + 1
        return result