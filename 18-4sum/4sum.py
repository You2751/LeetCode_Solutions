class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if(len(nums) < 4):
            return []
        result = []
        nums.sort()
        for idx in range(len(nums) - 3):
            if(idx > 0 and nums[idx] == nums[idx - 1]):
                continue
            for idx2 in range(idx + 1, len(nums) - 2):
                if(idx2 > idx + 1 and nums[idx2] == nums[idx2 - 1]):
                    continue
                left, right = idx2 + 1, len(nums) - 1
                while(left< right):
                    check_sum = nums[idx] + nums[idx2] + nums[left] + nums[right]
                    if(check_sum == target):
                        result.append([nums[idx], nums[idx2], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while(left < right and nums[left] == nums[left - 1]):
                            left += 1
                        while(right > left and right + 1 < len(nums) and nums[right] == nums[right + 1]):
                            right -= 1
                    elif(check_sum > target):
                        right -= 1
                    elif(check_sum < target):
                        left += 1
        return result