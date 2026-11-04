class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        result = []
        n = len(nums)
        counter = Counter(nums)
        counter = dict(sorted(counter.items(), key = lambda x:(x[0])))
        while(n):
            n -= 1
            for key, val in counter.items():
                if(val):
                    result.append(key)
                    counter[key] -= 1
        return result