class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        counter = defaultdict(int)
        result, pairs, right = 0, 0, -1
        for left in range(len(nums)):
            while(pairs < k and right + 1 < len(nums)):
                right += 1
                pairs += counter[nums[right]]
                counter[nums[right]] += 1
            if(pairs >= k):
                result += n - right
            counter[nums[left]] -= 1
            pairs -= counter[nums[left]]
        return result