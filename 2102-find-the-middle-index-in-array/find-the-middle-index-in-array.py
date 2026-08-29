class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        left_sum = 0
        right_sum = sum(nums)
        
        for right in range(len(nums)):
            right_sum -= nums[right]
            if(left_sum == right_sum): return right
            left_sum += nums[right]
        return -1