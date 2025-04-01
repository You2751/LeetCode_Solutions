class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        odd_count = 0
        if(k > len(s)):
            return False
        if(k == len(s)):
            return True
        counter = Counter(s)
        for count in counter.values():
            if(count % 2):
                odd_count += 1
        return odd_count <= k