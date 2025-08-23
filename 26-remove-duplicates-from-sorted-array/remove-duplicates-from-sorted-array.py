class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        for right in range(len(nums)):
            if(right == 0 or nums[right] != nums[right - 1]):
                nums[left] = nums[right]
                left += 1
        return left