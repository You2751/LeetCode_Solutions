class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nums = list(str(n))
        right = len(nums) - 1
        while(right > 0 and nums[right - 1] >= nums[right]):
            right -= 1
        if(right == 0):
            return -1
        swap_idx = len(nums) - 1
        while(swap_idx > right - 1 and nums[right - 1] >= nums[swap_idx]):
            swap_idx -= 1
        nums[right - 1], nums[swap_idx] = nums[swap_idx], nums[right - 1]
        nums[right:] = nums[right:][::-1]
        result = int("".join(nums))
        return result if result <= 2**31 - 1 else -1