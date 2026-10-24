class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        result = []
        n = len(nums)
        counter = Counter(nums)
        for key, val in counter.items():
            if(val < k):
                result += [key] * val
            else:
                result += [key] * k
        return result