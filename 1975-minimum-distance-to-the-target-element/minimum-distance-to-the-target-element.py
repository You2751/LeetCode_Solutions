class Solution:
    def getMinDistance(self, nums: list[int], target: int, start: int) -> int:
        result = float('inf')
        for idx, num in enumerate(nums):
            if(num == target):
                result = min(result, abs(idx - start))
        return result