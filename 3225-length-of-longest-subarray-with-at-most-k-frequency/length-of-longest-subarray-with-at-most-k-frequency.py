class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        counter = defaultdict(int)
        result = left = 0
        for right, num in enumerate(nums):
            counter[num] += 1
            while(counter[num] > k):
                counter[nums[left]] -= 1
                left += 1
            result = max(result, right - left + 1)
        return result