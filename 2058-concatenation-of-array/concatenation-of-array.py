class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [None] * 2 * n
        idx = 0 
        for idx in range(2*n):
            result[idx] = nums[idx % n]
        return result