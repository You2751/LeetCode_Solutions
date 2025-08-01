class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        sorted_nums = sorted(nums)
        median = (len(nums) + 1) // 2
        small_half = sorted_nums[:median][::-1]
        big_half = sorted_nums[median:][::-1]
        even, odd = 0, 1
        ptr1 = ptr2 = 0
        while(ptr1 < len(small_half)):
            nums[even] = small_half[ptr1]
            even += 2
            ptr1 += 1
        while(ptr2 < len(big_half)):
            nums[odd] = big_half[ptr2]
            odd += 2
            ptr2 += 1