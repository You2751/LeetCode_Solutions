class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if not k:
            return 0
        left = result = 0
        prod = 1
        for right in range(len(nums)):
            prod *= nums[right]
            while(prod >= k and left <= right):
                prod /= nums[left]
                left += 1
            result += right - left + 1
        return result
        