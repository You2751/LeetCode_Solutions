class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        count = left = 0
        for right in range(n // 2, n):
            if(left < n // 2):
                if(2 * nums[left] <= nums[right]):
                    left += 1
                    count += 2
            else:
                break
        return count