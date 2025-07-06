class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if(k <= 0):
            return 0
        left = result = 0
        prod = 1
        for right, num in enumerate(nums):
            prod *= num
            while(prod >= k and left <= right):
                prod /= nums[left]
                left += 1
            result += right - left + 1
        return result