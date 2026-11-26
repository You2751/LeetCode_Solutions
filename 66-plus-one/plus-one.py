class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        num = 0
        result = []
        for digit in digits:
            num *= 10
            num += digit
        num += 1
        while(num):
            digit = num % 10
            result.append(digit)
            num //= 10
        return result[::-1]