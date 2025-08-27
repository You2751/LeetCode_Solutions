class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while(left + 1 < len(nums) and nums[left] <= nums[left + 1]):
            left += 1
        if(left == len(nums) - 1):
            return 0
        while(right - 1 >= 0 and nums[right] >= nums[right - 1]):
            right -=1
        window_min = min(nums[left:right + 1])
        window_max = max(nums[left:right + 1])
        while(left > 0 and nums[left - 1] > window_min):
            left -= 1
        while(right  + 1 < len(nums) and window_max > nums[right + 1]):
            right += 1
        return right - left + 1