class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        result = white = blocks[:k].count('W')
        for i in range(k, len(blocks)):
            white += 1 if blocks[i] == 'W' else 0
            white -= 1 if blocks[i - k] == 'W' else 0
            result = min(result, white)
        return result