class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        result = left = ones = zeros = 0
        for right in range(len(s)):
            if(s[right] == '1'):
                ones += 1
            elif(s[right] == '0'):
                zeros += 1
            while(ones > k and zeros > k):
                if(s[left] == '1'):
                    ones -= 1
                elif(s[left] == '0'):
                    zeros -= 1
                left += 1
            result += right - left + 1
        return result