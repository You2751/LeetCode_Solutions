class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        result = 0
        check_set = set(nums)
        for num in set(nums):
            if((num - 1) not in check_set):
                length = 1
                while((num + length) in check_set):
                    length += 1
                result = max(result, length)
        return result
