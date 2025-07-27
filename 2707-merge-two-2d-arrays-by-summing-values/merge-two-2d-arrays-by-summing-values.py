class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        dic = defaultdict(int)
        for key, val in nums1:
            dic[key] += val
        for key, val in nums2:
            dic[key] += val
        result = []
        for key, val in dic.items():
            result.append([key, val])
        result.sort(key = lambda x:(x[0], x[1]))
        return result