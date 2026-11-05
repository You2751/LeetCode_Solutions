class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        seen = {0}
        idx = 0
        turn = 1
        while(True):
            idx = (idx + (turn * k)) % n
            if(idx in seen):
                break
            seen.add(idx)
            turn += 1
        return [i + 1 for i in range(n) if i not in seen]