class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        counter = Counter(nums)
        values = sorted(counter)
        print(values)
        for idx in range(len(values) - 1):
            for idx2 in range(idx + 1, len(values)):
                if(counter[values[idx]] != counter[values[idx2]]):
                    return [values[idx], values[idx2]]

        return [-1, -1]