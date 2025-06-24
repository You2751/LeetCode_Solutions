class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        if(len(s) < 3):
            return 0
        left = result = 0
        counter = defaultdict(int)        
        for right, c in enumerate(s):
            counter[c] += 1
            while(all(counter[c] for c in 'abc')):
                result += len(s) - right
                counter[s[left]] -= 1
                left += 1
        return result