class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        result = 0
        n = len(nums)
        if(n < 3):
            return result
        nums.sort()
        closest_sum = float('inf')
        for idx in range(n - 2):
            left, right = idx + 1, n - 1
            while(left < right):
                check_sum = nums[idx] + nums[left] + nums[right]
                if(check_sum == target):
                    return check_sum
                elif(check_sum > target):
                    right -=  1
                else:
                    left += 1
                if(abs(check_sum - target) < abs(closest_sum - target)):
                    closest_sum = check_sum
        return closest_sum