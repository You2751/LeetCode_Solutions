class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2_with_idx = [[num, idx] for idx, num in enumerate(nums2)]
        result = [0] * len(nums2_with_idx)
        nums2_with_idx.sort()
        left, right = 0, len(nums1) - 1
        for num in nums1:
            if(nums2_with_idx[left][0] < num):
                result[nums2_with_idx[left][1]] = num
                left += 1
            else:
                result[nums2_with_idx[right][1]] = num
                right -= 1
        return result