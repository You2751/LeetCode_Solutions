class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums) - 2):
            if(nums[i] == 0):
                nums[i + 2] ^= 1
                nums[i + 1] ^= 1
                nums[i] ^= 1
                count += 1
        one_counter = nums.count(1)
        if(one_counter == len(nums)):
            return count
        return -1