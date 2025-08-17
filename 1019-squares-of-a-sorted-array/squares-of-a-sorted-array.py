class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        result = [None] * len(nums)
        for idx in range(len(nums) - 1, -1, -1):
            left_val = nums[left] ** 2
            right_val = nums[right] ** 2
            if(left_val < right_val):
                result[idx] = right_val
                right -= 1
            else:
                result[idx] = left_val
                left += 1
        return result