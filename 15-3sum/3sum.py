class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        nums.sort()
        for idx in range(len(nums) - 2):
            if(nums[idx] > 0):
                return result
            if(idx > 0 and nums[idx] == nums[idx - 1]):
                continue
            left, right = idx + 1, len(nums) - 1
            while(left < right):
                check_sum = nums[idx] + nums[left] + nums[right]
                if(check_sum == 0):
                    result.append([nums[idx], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while(left < right and nums[left] == nums[left - 1]):
                        left += 1
                    while(right > left and right + 1 <n and nums[right] == nums[right + 1]):
                        right -= 1
                elif(check_sum > 0):
                    right -= 1
                else:
                    left += 1
        return result