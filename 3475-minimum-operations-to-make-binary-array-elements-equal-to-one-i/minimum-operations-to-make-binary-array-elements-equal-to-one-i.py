class Solution:
    def minOperations(self, nums: List[int]) -> int:
        flips = 0
        for i in range(len(nums) - 2):
            if(not nums[i]):
                nums[i] ^= 1
                nums[i + 1] ^= 1
                nums[i + 2] ^= 1
                flips += 1
        ones = nums.count(1)
        if(ones == len(nums)):
            return flips
        return -1