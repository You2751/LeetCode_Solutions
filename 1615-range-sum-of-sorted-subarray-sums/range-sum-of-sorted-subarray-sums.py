class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        array = []
        mod = 10**9 + 7
        for i in range(len(nums)):
            prefix = 0
            for j in range(i, len(nums)):
                prefix += nums[j]
                array.append(prefix)
        array.sort()
        return sum(array[left - 1:right]) % mod