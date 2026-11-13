class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        result = float('inf')
        min_left = [float('inf')] * (n + 1)
        min_right = [float('inf')] * (n + 1)
        for i in range(n):
            min_left[i + 1] = min(min_left[i], nums[i]) 
        for i in range(n - 1, -1, -1):
            min_right[i] = min(min_right[i + 1], nums[i])
        
        for i in range(n):
            if(min_left[i] < nums[i] > min_right[i]):
                result = min(result, min_left[i] + nums[i] + min_right[i])
        if(result != float('inf')):
            return result
        return -1