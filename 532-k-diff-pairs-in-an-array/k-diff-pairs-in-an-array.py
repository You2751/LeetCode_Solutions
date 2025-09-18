class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        result = 0
        counter = Counter(nums)
        for key, val in counter.items():
            if(k == 0):
                if(val > 1):
                    result += 1
            else:
                if(key + k in counter):
                    result += 1
        return result