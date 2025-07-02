class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        result = 0
        counter = defaultdict(int)
        for i in range(len(s) - minSize + 1):
            string = s[i:i + minSize]
            chars = len(set(string))
            if(chars <= maxLetters):
                counter[string] += 1
                result = max(result, counter[string])
        return result