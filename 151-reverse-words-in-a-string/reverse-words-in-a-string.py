class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        s = s.split(" ")
        left, right = 0, len(s) - 1
        while(left < right):
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        result = s[0]
        if(len(s) >= 1):
            for word in s[1:]:
                if(word != ""):
                    result += " " + word
        return result