class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ptr = left = 0
        right = len(nums) - 1
        while(ptr <= right):
            if(nums[ptr] == 0):
                nums[ptr], nums[left] = nums[left], nums[ptr]
                ptr += 1
                left += 1
            elif(nums[ptr] == 1):
                ptr += 1
            else:
                nums[ptr], nums[right] = nums[right], nums[ptr]
                right -= 1
