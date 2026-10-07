class Solution:
    def minOperations(self, s: str) -> int:
        count = 0
        for idx, c in enumerate(s):
            if(idx % 2 == 0):
                expected = "0"
            else:
                expected = "1"
            if(c != expected):
                count += 1
        return min(count, len(s) - count)