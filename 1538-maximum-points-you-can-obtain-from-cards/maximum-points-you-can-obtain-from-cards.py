class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left_sum = result = sum(cardPoints[:k])
        right_idx = len(cardPoints)
        right_sum = 0
        for idx in range(k - 1, -1, -1):
            right_idx -= 1
            right_sum += cardPoints[right_idx]
            left_sum -= cardPoints[idx]
            result = max(result, left_sum + right_sum)
        return result