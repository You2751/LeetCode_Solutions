class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        pairs = 0
        check = Counter(nums)
        
        for key, val in check.items():
            if(val > 1):
                pairs += (val) * (val - 1)
        return pairs // 2