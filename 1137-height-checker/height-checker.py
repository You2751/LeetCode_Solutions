class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        checks = 0
        sorted_heights = sorted(heights)
        for idx, h in enumerate(heights):
            if(h != sorted_heights[idx]):
                checks += 1
        return checks 