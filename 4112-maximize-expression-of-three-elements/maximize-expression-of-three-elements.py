class Solution:
    def maximizeExpressionOfThree(self, nums: List[int]) -> int:
        min_val = float('inf')
        max_first = max_second = float('-inf')
        for num in nums:
            if(num < min_val):
                min_val = num
            if(num > max_first):
                max_second = max_first
                max_first = num
            elif(num > max_second):
                max_second = num
        return max_first + max_second - min_val