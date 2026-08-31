class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        result = []
        nums = []
        for arr in grid:
            for num in arr:
                nums.append(num)
        print(nums)
        for num in nums:
            idx = abs(num) - 1
            if(nums[idx] > 0):
                nums[idx] = -nums[idx]
            else:
                result.append(abs(num))
        return result + [i + 1 for i, num in enumerate(nums) if num > 0]