class Solution:
    def isBoomerang(self, points: list[list[int]]) -> bool:
        seen = set()
        prev_x = prev_y = None
        for idx, (x, y) in enumerate(points):
            if((x, y) in seen):
                return False
            seen.add((x, y))
            if(prev_x is not None):
                dx = x - prev_x
                dy = y - prev_y
                slope = dy / dx if dx != 0 else float('inf')
                if(slope in seen):
                    return False
                seen.add(slope)
            prev_x, prev_y = x, y
        return True