class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        if(len(nums) < 4):
            return 0
        result = float('inf')
        result = min(b - a for a, b in zip(nums[:4], nums[-4:]))
        return result