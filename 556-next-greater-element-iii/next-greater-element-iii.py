class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nums = list(str(n))
        length = len(nums)
        right = length - 1
        while(right - 1 >= 0 and nums[right - 1] >= nums[right]):
            right -= 1
        if(right == 0):
            return -1
        check_idx =  length - 1
        while(check_idx > right and nums[right - 1] >= nums[check_idx]):
            check_idx -= 1
        nums[right - 1], nums[check_idx] = nums[check_idx], nums[right - 1]
        nums[right:] = nums[right:][::-1]
        result = int("".join(nums))
        return result if result <= 2**31 - 1 else -1