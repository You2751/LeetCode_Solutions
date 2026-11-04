class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        result = 0
        n = len(nums)
        prefix = [0] * (n + 1)
        for idx, num in enumerate(nums):
            prefix[idx + 1] = prefix[idx] + nums[idx]
        print(prefix)
        for idx, num in enumerate(nums[:-1]):
            total = prefix[-1] - prefix[idx + 1]
            print("total", total)
            count = n - idx - 1
            if(num * count > total):
                result += 1
        return result