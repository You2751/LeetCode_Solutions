class Solution:
    def reverseWords(self, s: str) -> str:
        result = ""

        arr = s.strip().split()
        arr.reverse()
        print(arr)
        for idx, word in enumerate(arr):
            if(" " in word):
                continue
            else:
                result += word + " "
        return result[:len(result) - 1]