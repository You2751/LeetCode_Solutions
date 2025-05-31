class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        swaps_one = self.min_swaps(nums, 1)
        return swaps_one
    def min_swaps(self, nums, target):
        total_count = nums.count(target)
        if(total_count in [0, len(nums)]):
            return 0
        extended = nums + nums[:total_count - 1]
        max_in_window = current = sum(extended[:total_count])
        for i in range(total_count, len(extended)):
            current += extended[i]
            current -= extended[i - total_count]
            max_in_window = max(current, max_in_window)
        return total_count - max_in_window
        