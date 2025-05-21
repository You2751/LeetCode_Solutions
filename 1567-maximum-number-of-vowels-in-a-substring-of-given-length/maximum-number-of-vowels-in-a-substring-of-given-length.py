class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        max_length = 0
        vowels = set('aeiou')
        counter = Counter()
        for i in range(k):
            if(s[i] in vowels):
                counter[s[i]] += 1
        result = sum(counter.values())
        for i in range(k, len(s)):
            if(s[i] in vowels):
                counter[s[i]] += 1
            if(s[i - k] in vowels):
                counter[s[i - k]] -= 1
            result = max(result, sum(counter.values()))
        return result