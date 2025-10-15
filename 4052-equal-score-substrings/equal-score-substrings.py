class Solution:
    def scoreBalance(self, s: str) -> bool:
        total_score = 0
        for c in s:
            total_score += (ord(c) - ord('a') + 1)
        half_score = total_score / 2
        for c in s:
            total_score -= (ord(c) - ord('a') + 1)
            if(total_score == half_score):
                return True
        return False