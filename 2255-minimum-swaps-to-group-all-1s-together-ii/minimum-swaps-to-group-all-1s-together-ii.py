class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        ones_count = nums.count(1)
        if(ones_count in [0, len(nums) - 1]):
            return 0
        nums_extended = nums + nums[:ones_count]
        curr_ones = max_ones = sum(nums_extended[:ones_count])
        for i in range(ones_count, len(nums_extended)):
            curr_ones += nums_extended[i]
            curr_ones -= nums_extended[i - ones_count]
            max_ones = max(max_ones, curr_ones)
        return ones_count - max_ones