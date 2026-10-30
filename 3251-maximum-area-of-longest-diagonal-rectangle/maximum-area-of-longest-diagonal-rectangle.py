class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_d = max_area = float('-inf')
        for l, w in dimensions:
            diagonal = math.sqrt(l**2 + w**2)
            print(diagonal)
            if(diagonal > max_d):
                max_d = max(max_d, diagonal)
                max_area = l * w
            elif(diagonal == max_d):
                max_area = max(max_area, l * w)
        return max_area