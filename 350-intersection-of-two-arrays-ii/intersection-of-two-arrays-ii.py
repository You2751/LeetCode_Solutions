class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        if not nums1 or not nums2:
            return result
        counter_nums1 = Counter(nums1)
        counter_nums2 = Counter(nums2)
        for key, val in counter_nums1.items():
            if(key in counter_nums2):
                result += [key] * min(val, counter_nums2[key])
        return result