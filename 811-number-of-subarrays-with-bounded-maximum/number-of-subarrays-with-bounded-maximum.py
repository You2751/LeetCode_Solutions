class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        result = count = start = 0
        for end, num in enumerate(nums):
            if(left <= num <= right):
                count = end - start + 1
            elif(num > right):
                start = end + 1
                count = 0
            result += count
        return result