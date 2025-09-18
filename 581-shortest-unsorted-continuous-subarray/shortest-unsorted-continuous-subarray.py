class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        left = 0
        n = len(nums)
        while(left + 1 < n and nums[left] <= nums[left + 1]):
            left += 1
        if(left == n - 1):
            return 0
        right = len(nums) - 1
        while(right > 0 and nums[right] >= nums[right - 1]):
            right -= 1
        window_min = min(nums[left:right + 1])
        window_max = max(nums[left:right + 1])

        while(left - 1 >= 0 and nums[left - 1] > window_min):
            left -= 1
        while(right + 1 < n and nums[right + 1]  < window_max):
            right += 1
        return right - left + 1