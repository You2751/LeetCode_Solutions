class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 0
        for num in nums:
            if(idx < 2 or num > nums[idx - 2]):
                nums[idx] = num
                idx += 1
        return idx