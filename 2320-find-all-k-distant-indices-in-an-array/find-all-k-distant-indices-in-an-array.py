class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        left = 0
        result = []
        n = len(nums)
        for right, num in enumerate(nums):
            if(num == key):
                left = max(left, right - k)
                while(left <= right + k and left < n):
                    result.append(left)
                    left += 1
        return result