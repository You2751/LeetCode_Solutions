class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        counter = Counter(s)
        if(len(counter) <= k):
            return 0
        deleted_count = 0
        unique_chars = len(counter)
        counter = sorted(counter.items(), key = lambda x:x[1])
        for key, val in counter:
            unique_chars -= 1
            deleted_count += val
            if(unique_chars <= k):
                return deleted_count