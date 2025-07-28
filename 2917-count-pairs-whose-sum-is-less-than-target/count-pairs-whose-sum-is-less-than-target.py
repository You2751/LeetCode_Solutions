class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        result = 0
        nums.sort()
        left, right = 0, len(nums) - 1
        while(left < right):
            summation = nums[left] + nums[right]
            if(summation < target):
                result += right - left
                left += 1
            else:
                right -= 1
        return result