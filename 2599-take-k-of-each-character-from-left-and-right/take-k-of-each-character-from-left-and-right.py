class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        counter = Counter(s)
        if any(counter[char] < k for char in "abc"):
            return -1 
        max_length = start_idx = 0
        for idx, ch in enumerate(s):
            counter[ch] -= 1
            while(counter[ch] < k):
                counter[s[start_idx]] += 1
                start_idx += 1
            max_length = max(max_length, idx - start_idx + 1)
        return len(s) - max_length
