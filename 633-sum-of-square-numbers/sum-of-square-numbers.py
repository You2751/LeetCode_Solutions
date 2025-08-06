class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left, right = 1, int(sqrt(c))
        if(right * right == c):
            return True
        while(left<= right):
            check_sum = left**2 + right**2
            if(check_sum > c):
                right -= 1
            elif(check_sum < c):
                left += 1
            elif(check_sum == c):
                return True
        return False