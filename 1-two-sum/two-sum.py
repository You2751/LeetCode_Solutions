class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dic = defaultdict(int)
        for idx, num in enumerate(nums):
            if((target - num) in dic):
                return [dic[target - num], idx]
            dic[num] = idx