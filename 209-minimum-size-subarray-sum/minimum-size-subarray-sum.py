class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        result = float('inf')
        left = running_sum = 0
        for right, num in enumerate(nums):
            running_sum += num
            while(running_sum >= target):
                result = min(result, right - left + 1)
                running_sum -= nums[left]
                left += 1
        if(result == float('inf')):
            return 0
        return result