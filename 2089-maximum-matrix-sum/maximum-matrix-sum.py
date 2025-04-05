class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        negative_nums = total_sum = 0
        min_val = float('inf')
        for row in matrix:
            for val in row:
                total_sum += abs(val)
                min_val = min(min_val, abs(val))

                if(val < 0):
                    negative_nums += 1
    
        if(not negative_nums % 2 or not min_val):
            return total_sum 
        return total_sum - (2 * min_val)