class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for idx, num in enumerate(nums):
            total = 0
            for c in str(num):
                total += int(c)
            if(total == idx):
                return idx
        return -1