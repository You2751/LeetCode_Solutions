class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if(sum(nums) < target):
            return 0
        left = running_sum = 0
        result = float('inf')
        for right, val in enumerate(nums):
            running_sum += val
            while(running_sum >= target):
                result = min(result, right - left + 1)
                running_sum -= nums[left]
                left += 1
        return result