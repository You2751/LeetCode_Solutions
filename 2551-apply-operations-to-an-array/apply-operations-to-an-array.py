class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            if(nums[i] == nums[i  - 1]):
                nums[i] = 0
                nums[i - 1] *= 2
        left = 0
        for right in range(len(nums)):
            if(nums[right] != 0):
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
        return nums