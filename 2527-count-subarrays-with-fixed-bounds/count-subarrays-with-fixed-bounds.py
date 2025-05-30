class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        result = 0
        last_min_idx = last_max_idx = last_out_of_bound = -1
        for idx, num in enumerate(nums):
            if(num < minK or num > maxK):
                last_out_of_bound = idx
            if(num == minK):
                last_min_idx = idx
            if(num == maxK):
                last_max_idx = idx
            result += max(0, min(last_max_idx, last_min_idx) - last_out_of_bound)
        return result