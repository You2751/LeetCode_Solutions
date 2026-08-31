class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        n = len(nums)
        counter = Counter(nums)
        for key, val in counter.items():
            if(val == 1 and n > 1):
                return False
            if(val % 2 == 1):
                return False
        return True