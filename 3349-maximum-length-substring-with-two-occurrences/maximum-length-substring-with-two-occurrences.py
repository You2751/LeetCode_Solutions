class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        counter = defaultdict(int)
        left = result = 0
        for right in range(len(s)):
            counter[s[right]] += 1
            while(counter[s[right]] == 3):
                counter[s[left]] -= 1
                left += 1
            result = max(result, right - left + 1)
        return result