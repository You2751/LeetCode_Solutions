class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        result = 0
        dic = defaultdict(int)
        for right, num in enumerate(nums):
            if((num - diff) in dic and (num - (2*diff)) in dic):
                result += 1
            dic[num] += 1
        return result
