class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        left = 0
        result = []
        for right, val in enumerate(nums):
            if(val == key):
                left = max(left, right - k)
                while(left <= right + k and left < len(nums)):
                    result.append(left)
                    left += 1
        return result