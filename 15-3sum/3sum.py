class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        if(len(nums) < 3):
            return result
        nums.sort()
        for idx in range(len(nums) - 2):
            if(idx > 0 and nums[idx] == nums[idx - 1]):
                continue 
            if(nums[idx] > 0):
                return result
            left, right = idx + 1, len(nums) - 1
            while(left < right):
                check = nums[idx] + nums[left] + nums[right]
                if(check > 0):
                    right -= 1
                elif(check < 0):
                    left += 1
                else:
                    result.append([nums[idx], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while(left < right and nums[left] == nums[left - 1]):
                        left += 1
                    while(right > left and right > 0 and right + 1 < len(nums) and nums[right] == nums[right + 1]):
                        right -= 1
        return result