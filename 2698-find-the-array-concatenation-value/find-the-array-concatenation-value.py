class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        def zeros(num):
            if(num == 0):
                return 1
            zeros = 0
            while(num):
                num //= 10
                zeros += 1
            return zeros
        left, right = 0, len(nums) - 1
        result = 0
        while(left <= right):
            if(left != right):
                print(nums[left])
                print(zeros(nums[right]))
                result += (nums[left] * (10 ** zeros(nums[right]))) + nums[right]
                print(result)
            else:
                result += nums[left]
            left += 1
            right -= 1
        return result 
            