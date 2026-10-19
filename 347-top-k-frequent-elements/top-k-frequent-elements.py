class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counter = Counter(nums)
        counter = sorted(counter.items(), key = lambda x:(-x[1], x[0]))
        return [key for key, val in counter[:k]]