class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        total_ones = nums.count(1)
        if(total_ones in [0, len(nums) - 1]):
            return 0
        nums_extended = nums + nums[:total_ones]
        max_ones = curr_ones = sum(nums_extended[:total_ones])
        for right in range(total_ones, len(nums_extended)):
            curr_ones += nums_extended[right]
            curr_ones -= nums_extended[right - total_ones]
            max_ones = max(curr_ones, max_ones)
        return total_ones - max_ones