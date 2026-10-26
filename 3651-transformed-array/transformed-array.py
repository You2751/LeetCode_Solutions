class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [None] * n
        for idx, num in enumerate(nums):
            if(not num):
                result[idx] = 0
            else:
                new_idx = (idx + num) % n 
                result[idx] = nums[new_idx]
        return result