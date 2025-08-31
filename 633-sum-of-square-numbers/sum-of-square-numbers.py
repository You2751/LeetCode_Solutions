class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left, right = 0, int(sqrt(c))
        while(left <= right):
            check_num = left**2 + right**2
            if(check_num == c):
                return True
            elif(check_num > c):
                right -= 1
            else:
                left += 1
        return False