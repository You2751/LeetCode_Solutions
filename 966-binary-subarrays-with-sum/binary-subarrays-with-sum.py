class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def at_most(target):
            if(target < 0):
                return 0
            left = curr_sum = result = 0
            for right, num in enumerate(nums):
                curr_sum += num
                while(curr_sum > target):
                    curr_sum -= nums[left]
                    left += 1
                result += right - left + 1
            return result
        return at_most(goal) - at_most(goal - 1)