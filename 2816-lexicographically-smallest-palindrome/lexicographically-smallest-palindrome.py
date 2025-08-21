class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        left, right = 0, len(s) - 1
        left_string = right_string = ""
        while(left <= right):
            if(left != right):
                if(s[left] == s[right]):
                    left_string += s[left]
                    right_string = s[right] + right_string
                    left += 1
                    right -= 1
                else:
                    min_char = min(s[left], s[right])
                    left_string += min_char
                    right_string = min_char + right_string
                    left += 1
                    right -= 1
            else:
                left_string += s[left]
                break
        return left_string + right_string