class Solution:
    def findLHS(self, nums: List[int]) -> int:
        result = 0
        counter = Counter(nums)
        for num in nums:
            if(num + 1 in counter):
                result = max(result, counter[num] + counter[num + 1])
        return result