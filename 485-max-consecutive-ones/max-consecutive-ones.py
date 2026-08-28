class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result = float('-inf')
        left = right = 0
        while(right < len(nums)):
            if(not nums[right]):
                result = max(result, right - left)
                left = right + 1
            right += 1
        result = max(result, right - left)
        return result