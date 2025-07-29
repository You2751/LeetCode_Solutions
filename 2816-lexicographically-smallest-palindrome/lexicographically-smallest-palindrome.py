class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        left_string = right_string = ""
        left, right = 0, len(s) - 1
        while(left <= right):
            if(left != right):
                if(s[left] == s[right]):
                    left_string += s[left]
                    right_string = s[right] + right_string
                    left += 1
                    right -= 1
                else:
                    char = min(s[left], s[right])
                    left_string += char
                    right_string = char + right_string
                    left += 1
                    right -= 1
            else:
                left_string += s[left]
                break
        return left_string + right_string