class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        counter = Counter(s)
        left = max_length = 0
        if(any(counter[char] < k for char in 'abc')):
            return -1
        for right, char in enumerate(s):
            counter[char] -= 1
            while(counter[char] < k):
                counter[s[left]] += 1
                left += 1
            max_length = max(max_length, right - left + 1)
        return len(s) - max_length