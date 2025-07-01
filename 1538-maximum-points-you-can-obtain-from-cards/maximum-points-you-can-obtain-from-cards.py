class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        result = left_sum = sum(cardPoints[:k])
        right_idx = len(cardPoints)
        right_sum = 0
        for idx in range(k - 1, -1, -1):
            right_idx -= 1
            right_sum += cardPoints[right_idx]
            left_sum -= cardPoints[idx]
            result = max(result, right_sum + left_sum)
        return result