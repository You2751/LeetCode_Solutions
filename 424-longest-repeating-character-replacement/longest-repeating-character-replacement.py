class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = defaultdict(int)
        max_freq = result = left = 0
        for right, ch in enumerate(s):
            counter[ch] += 1
            max_freq = max(max_freq, counter[ch])
            while(right - left + 1 > max_freq + k): 
                max_freq = max(counter.values())
                counter[s[left]] -= 1
                left += 1
            result = max(result, right - left + 1)
        return result