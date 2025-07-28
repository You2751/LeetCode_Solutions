class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        check = set()
        result = float('-inf')
        for val in nums:
            if(val > 0 and (-1 * val) in check):
                result = max(result, abs(val))
            if(val < 0 and (-1 * val) in check):
                result = max(result, abs(val))
            check.add(val)
        return result if result != float('-inf') else -1