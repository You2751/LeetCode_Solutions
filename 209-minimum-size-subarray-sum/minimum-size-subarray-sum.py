class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        result = float('inf')
        total = left = 0
        for right in range(len(nums)):
            total += nums[right]
            while(total >= target):
                result = min(result, right - left + 1)
                total -= nums[left]
                left += 1
        if(result == float('inf')):
            return 0
        return result