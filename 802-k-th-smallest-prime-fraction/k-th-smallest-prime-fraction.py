class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        nums = []
        for left in range(len(arr)):
            for right in range(left, len(arr)):
                nums.append([arr[left] / arr[right], str(arr[left]) + "/" + str(arr[right])])
        nums.sort(key = lambda x:x[0])
        result = nums[k - 1][1].split('/')
        return [int(result[0]), int(result[1])]