class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        array = []
        n = len(nums)
        mod = 10**9 + 7
        for i in range(n):
            curr_sum = 0
            for j in range(i, n):
                curr_sum += nums[j]
                array.append(curr_sum)
        array.sort()
        return sum(array[left - 1:right]) % mod