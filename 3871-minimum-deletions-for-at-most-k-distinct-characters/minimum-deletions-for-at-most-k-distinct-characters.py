class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        counter = Counter(s)
        if(len(counter) <= k):
            return 0
        distinct_chars = len(counter)
        deleted_chars = result = 0
        counter = sorted(counter.items(), key = lambda x:x[1])
        for c, val in counter:
            deleted_chars += val
            distinct_chars -= 1
            if(distinct_chars <= k):
                return deleted_chars