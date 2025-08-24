class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.strip().split()
        arr.reverse()
        return " ".join(arr)