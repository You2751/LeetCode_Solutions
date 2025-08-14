class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = float('-inf')
        for idx, height in enumerate(heights):
            start = idx
            while(stack and stack[-1][-1] >= height):
                index, height_right = stack.pop()
                max_area = max(max_area, height_right * (idx - index))
                start = index
            stack.append([start, height])
        
        for i, height in stack:
            max_area = max(max_area, height * (len(heights) - i))
        return max_area