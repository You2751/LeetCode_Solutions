class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        idx = 0
        for ch in str1:
            ch_next = 'a' if ch == 'z' else chr(ord(ch) + 1)
            if(idx < len(str2) and str2[idx] in (ch, ch_next)):
                idx += 1
        return idx == len(str2)