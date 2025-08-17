class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        result = ''
        ch_idx = 0
        for idx, c in enumerate(word):
            if(ch == c):
                ch_idx == idx
                result = word[:idx + 1]
                break
        if(result != ''):          
            return result[::-1] + word[idx + 1:]
        return word
