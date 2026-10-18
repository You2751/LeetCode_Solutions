class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        result = []
        set_nums1 = {val for val in nums1}
        set_nums2 = {val for val in nums2}
        def find_unique(nums, set_num):
            seen = set()
            sub_result = []
            for num in nums:
                if num not in set_num and num not in seen:
                    sub_result.append(num)
                    seen.add(num)
            return sub_result
        result.append(find_unique(nums1, set_nums2))
        result.append(find_unique(nums2, set_nums1))
        return result 