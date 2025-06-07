class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        result = 0
        left, right = 0, 1
        while(right < len(nums)):
            diff = nums[right] - nums[left]
            if(diff == 1):
                result = max(result, right - left + 1)
            if(diff <= 1):
                right += 1
            else:
                left += 1
        return result