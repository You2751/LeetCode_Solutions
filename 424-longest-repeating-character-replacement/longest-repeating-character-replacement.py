class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = defaultdict(int)
        result = left = max_char = 0
        for right, ch in enumerate(s):
            counter[ch] += 1
            max_char = max(max_char, counter[ch])
            if(right - left + 1 > max_char + k):
                counter[s[left]] -= 1
                if(counter[s[left]] == 0):
                    del counter[s[left]]
                left += 1
            result = max(result, right - left + 1)
        return result