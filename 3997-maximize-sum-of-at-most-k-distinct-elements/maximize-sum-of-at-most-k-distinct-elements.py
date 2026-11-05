class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        result = []
        counter = Counter(nums)
        counter = sorted(counter.items(), key = lambda x:[-x[0], x[1] == 1])
        for key, val in counter[:k]:
            result.append(key)
        return result