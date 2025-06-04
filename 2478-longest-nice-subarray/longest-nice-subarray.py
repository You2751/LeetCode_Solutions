class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        left = bit_mask = result = 0
        for right, num in enumerate(nums):
            while(bit_mask & num):
                bit_mask ^= nums[left]
                left += 1
            result = max(result, right - left + 1)
            bit_mask |= num
        return result