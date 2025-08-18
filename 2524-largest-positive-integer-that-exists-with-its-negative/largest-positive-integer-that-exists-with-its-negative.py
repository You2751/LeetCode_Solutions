class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        left, right = 0, len(nums) - 1
        while(left < right):
            check = nums[left] + nums[right]
            if(check == 0):
                return nums[right]
            elif(check > 0):
                right -= 1
            else:
                left += 1
        return -1
