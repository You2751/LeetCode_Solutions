class Solution:
    def kLengthApart(self, nums: list[int], k: int) -> bool:
        n = len(nums)
        prev_idx = None
        for idx, num in enumerate(nums):
            if(num == 1 and prev_idx and idx - prev_idx  - 1 < k):
                return False
            if(num == 1 and idx != n - 1):
                prev_idx = idx
        if(nums[-1] == 1 and n - prev_idx - 2 < k):
            return False
        return True
    