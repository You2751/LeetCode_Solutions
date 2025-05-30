class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.sliding_window_helper(nums, k) - self.sliding_window_helper(nums, k - 1)

    def sliding_window_helper(self, nums, k):
        result = left = 0
        counter = defaultdict(int)
        for right, num in enumerate(nums):
            counter[num] += 1
            while(len(counter) > k):
                counter[nums[left]] -= 1
                if(counter[nums[left]] == 0):
                    del counter[nums[left]]
                left += 1
            result += right - left + 1
        return result