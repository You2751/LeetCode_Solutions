class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        left = ones = zeros = result = 0
        for right in range(len(s)):
            if(s[right] == '1'):
                ones += 1
            else:
                zeros += 1
            while(zeros > k and ones > k):
                if(s[left] == '1'):
                    ones -= 1
                else:
                    zeros -= 1
                left += 1
            result += right - left + 1
        return result