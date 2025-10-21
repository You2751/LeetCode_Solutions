class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        set_nums = set(nums)
        m = 1
        candidate = m * k 
        while(candidate in set_nums):
            m += 1
            candidate = m * k 
        else:
            return candidate
        