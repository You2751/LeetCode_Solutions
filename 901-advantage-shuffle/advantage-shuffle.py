class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2_index = [[val, i] for i, val in enumerate(nums2)]
        nums2_index.sort(key = lambda x:(x[0], x[1]))
        nums1.sort()
        left, right  = 0, len(nums2) - 1 
        result = [0] * len(nums1)
        for num in nums1:
            if(num > nums2_index[left][0]):
                result[nums2_index[left][1]] = num
                left += 1
            else:
                result[nums2_index[right][1]] = num
                right -= 1
        return result