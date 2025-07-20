class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        a, b, c = sorted([a, b, c])
        
        left_gap = b - a - 1
        right_gap = c - b - 1
        max_steps = left_gap + right_gap
        if(left_gap == 0 and right_gap == 0):
            min_steps = 0
        elif(left_gap <= 1 or right_gap <= 1):
            min_steps = 1
        else:
            min_steps = 2
        return [min_steps, max_steps]