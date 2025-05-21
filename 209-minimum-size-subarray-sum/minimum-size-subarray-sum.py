class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if(sum(nums) < target):
            return 0
        result = float('inf')
        left = running_sum = 0
        for right in range(len(nums)):
            running_sum += nums[right]
            while(running_sum >= target):
                result = min(result, right - left + 1)
                running_sum -= nums[left] 
                left += 1
        return result