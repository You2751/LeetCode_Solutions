class Solution:
    def countBadPairs(self, nums: list[int]) -> int:
        good_pairs = 0
        n = len(nums)
        total_pairs = (n *(n - 1)) // 2
        dic = defaultdict(int)
        for i, num  in enumerate(nums):
            good_pairs += dic[num  - i]
            dic[num - i] += 1
        return total_pairs - good_pairs