class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        result = 0
        n = len(nums)
        min_vals = [0] * n
        max_vals = [0] * n

        min_vals[0] = nums[0]
        for i in range(1, n):
            min_vals[i] = min(min_vals[i - 1], nums[i])
        
        max_vals[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            max_vals[i] = max(max_vals[i + 1], nums[i])

        i = j = 0
        while(i < n and j < n):
            if(min_vals[i] <= max_vals[j]):
                result = max(result, j - i)
                j +=1
            else:
                i += 1
        return result