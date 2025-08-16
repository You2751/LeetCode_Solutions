class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        transposed_matrix = [list(row) for row in zip(*matrix)]

        return transposed_matrix