class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        groups = []
        n = len(s)
        left = result = 0
        while(left < n):
            count = 1
            while(left + 1 < n and s[left + 1] == s[left]):
                left += 1
                count += 1
            groups.append(count)
            left += 1
        for right in range(1, len(groups)):
            result += min(groups[right], groups[right - 1])
        return result