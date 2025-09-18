class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        left = 0
        n = len(nums)
        while(left + 1 < n and nums[left + 1] >= nums[left]):
            left += 1
        if(left == n - 1):
            return 0
        right = n - 1
        while(right - 1 >= 0 and nums[right] >= nums[right - 1]):
            right -= 1
        min_window = min(nums[left:right + 1])
        max_window = max(nums[left:right + 1])

        while(left - 1 >= 0 and nums[left - 1] > min_window):
            left -= 1

        while(right + 1 < n and nums[right + 1] < max_window):
            right += 1
        
        return right - left + 1