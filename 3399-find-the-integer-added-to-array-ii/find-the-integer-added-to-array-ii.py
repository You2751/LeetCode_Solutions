class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        result = float('inf')

        def is_valid_difference(diff):
            ptr1 = ptr2 = mis_matches = 0
            while(ptr1 < len(nums1) and ptr2 < len(nums2)):
                if(nums1[ptr1] + diff == nums2[ptr2]):
                    ptr1 += 1
                    ptr2 += 1
                else:
                    ptr1 += 1
                    mis_matches += 1
            return mis_matches <= 2
        
        for i in range(3):
            diff = nums2[0] - nums1[i]
            if(is_valid_difference(diff)):
                result = min(result, diff)
        
        return result