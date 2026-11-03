class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        prefix = [float("-inf")] * (n + 1)
        suffix = [float("inf")] * (n + 1)
        for idx, num in enumerate(nums):
            prefix[idx + 1] = max(prefix[idx], num)
        print(prefix)
        for idx in range(n - 1, -1, -1):
            suffix[idx] = min(suffix[idx + 1], nums[idx])
        result = float('inf')
        min_score = float('inf')
        for idx, num in enumerate(nums):
            score = prefix[idx + 1] - suffix[idx]
            min_score = min(min_score, score)
            if(min_score <= k):
                result = min(result, idx)
        if(result == float("inf")):
            return -1
        return result