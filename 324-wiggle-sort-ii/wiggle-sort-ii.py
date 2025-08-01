class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        sorted_nums = sorted(nums)
        median = (n + 1) // 2
        small_half = sorted_nums[:median][::-1]
        big_half = sorted_nums[median:][::-1]
        nums = self.insert_val(0, nums, small_half)
        nums = self.insert_val(1, nums, big_half)
    def insert_val(self, array_idx, array, even_odd_array):
        ptr = 0
        while(ptr < len(even_odd_array)):
            array[array_idx] = even_odd_array[ptr]
            array_idx += 2
            ptr += 1
        return array