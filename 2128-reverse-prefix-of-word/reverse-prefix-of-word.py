class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        idx = -1
        for index, char in enumerate(word):
            if(char == ch):
                idx = index
                break
        if(idx == -1):
            return word
        result = word[:idx + 1][::-1] + word[idx + 1:]
        return result