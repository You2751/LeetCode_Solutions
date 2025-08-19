class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        result = []
        left = 0
        for right in range(len(nums)):
            if(nums[right] == key):
                left = max(left, right - k)
                while(left <= right + k and left < len(nums)):
                    result.append(left)
                    left += 1
        return result