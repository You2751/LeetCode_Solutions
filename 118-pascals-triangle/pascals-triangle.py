class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rows = [[1] * row for row in range(1, numRows + 1)]
        idx = 2
        for row in rows[2:]:
            prev_row = rows[idx - 1]
            for i in range(1, len(prev_row)):
                if(i < len(row) - 1):
                    row[i] = prev_row[i] + prev_row[i - 1]
            idx += 1
        return rows