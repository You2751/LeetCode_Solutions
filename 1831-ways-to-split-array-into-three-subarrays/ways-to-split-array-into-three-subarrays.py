class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        n = len(nums)
        if(n < 3):
            return 0
        result = 0
        mod = (10**9 + 7)
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
        total_sum = prefix_sum[n]
        middle_idx = final_idx = 2
        for first_idx in range(1, n - 1):
            left_sum = prefix_sum[first_idx]

            if(middle_idx < first_idx + 1):
                middle_idx = first_idx + 1
            if(final_idx < first_idx + 1):
                final_idx = first_idx + 1
            
            while(middle_idx < n and prefix_sum[middle_idx] < 2 * left_sum):
                middle_idx += 1
            
            while(final_idx < n and prefix_sum[final_idx] <= (total_sum + left_sum) / 2):
                final_idx += 1
            
            if(final_idx > middle_idx):
                result = (result + (final_idx - middle_idx)) % mod
        return result