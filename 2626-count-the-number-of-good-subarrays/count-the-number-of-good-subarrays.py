class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        counter = defaultdict(int)
        left = pairs = result = 0
        for right, num in enumerate(nums):
            counter[num] += 1
            pairs += counter[num] - 1
            while(pairs >= k):
                result += len(nums) - right
                pairs -= counter[nums[left]] - 1
                counter[nums[left]] -= 1
                left += 1
        return result