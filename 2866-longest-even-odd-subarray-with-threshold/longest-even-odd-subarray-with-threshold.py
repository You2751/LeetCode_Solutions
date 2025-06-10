class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        left = result = 0
        while(left < n):
            if(nums[left] % 2 or nums[left] > threshold):
                left += 1
            else:
                right = left
                while(right < n and nums[right] <= threshold and (right == left or nums[right] % 2 != nums[right - 1] % 2)):
                    right += 1
                result = max(result, right - left)
                left += 1
        return result