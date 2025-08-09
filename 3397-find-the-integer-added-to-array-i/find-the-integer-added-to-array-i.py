class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        counter = defaultdict(int)
        for n1 in nums1:
            for n2 in nums2:
                counter[n2 - n1] += 1
        return max(counter, key = counter.get)