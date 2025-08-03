class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        counter = Counter(nums)
        result = 0
        if not k:
            for key, val in counter.items():
                if(val > 1):
                    result += 1
        else:
            for key, val in counter.items():
                if(key + k in counter):
                    result += 1
        return result