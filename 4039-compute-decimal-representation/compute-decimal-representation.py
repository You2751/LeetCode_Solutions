class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        result = []
        power = 0
        while(n):
            digit = n % 10
            if(digit):
                result.append(digit * (10 ** power))
            n //= 10
            power += 1
        return result[::-1]