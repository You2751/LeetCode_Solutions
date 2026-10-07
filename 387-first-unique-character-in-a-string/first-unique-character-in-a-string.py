class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = set()
        for idx, c in enumerate(s):
            if(c not in s[idx + 1:] and c not in seen):
                return idx
            seen.add(c)
        return -1