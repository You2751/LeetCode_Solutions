class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if(sum(nums) < target or target == 0):
            return 0
        left = curr_sum = 0
        result = float('inf')
        for right, num in enumerate(nums):
            curr_sum += num
            while(curr_sum >= target):
                result = min(result, right - left + 1)
                curr_sum -= nums[left]
                left += 1
        return result