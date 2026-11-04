class Solution:
    def minAbsoluteDifference(self, nums: list[int]) -> int:
        result = float('inf')
        ones, twos = [], []
        for idx, num in enumerate(nums):
            if(num == 1):
                ones.append(idx)
            elif(num == 2):
                twos.append(idx)
        if not twos or not ones:
            return -1
        for two in twos:
            for one in ones:
                result = min(result, abs(one - two))
        return result