class Solution:
    def minimumLength(self, s: str) -> int:
        deleted_chars = 0
        counter = Counter(s)
        print(counter)
        if not counter:
            return 0
        for c in counter.keys():
            if(counter[c] % 2 == 0):
                deleted_chars += counter[c] - 2
            else:
                deleted_chars += counter[c] - 1
        print(deleted_chars)
        return len(s) - deleted_chars