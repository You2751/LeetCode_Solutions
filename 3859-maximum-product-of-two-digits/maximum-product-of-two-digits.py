class Solution:
    def maxProduct(self, n: int) -> int:
        max1 = max2 = float('-inf')
        while(n):
            num = n % 10
            if(num > max1):
                max2 = max1
                max1 = num
            elif(num > max2):
                max2 = num
            n //= 10
        return max1 * max2