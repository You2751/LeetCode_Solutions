class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        counter = Counter(nums)
        middle = len(nums) // 2
        return counter[nums[middle]] == 1
