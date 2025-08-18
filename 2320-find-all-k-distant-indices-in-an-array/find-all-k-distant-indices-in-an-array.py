class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        left = 0
        result = []

        for right, num in enumerate(nums):
            if(num == key):
                left = max(left, right - k)
                while(left < len(nums) and left <= right + k):
                    result.append(left)
                    left += 1
        return result