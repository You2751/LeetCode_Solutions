class Solution:
    def minOperations(self, boxes: str) -> list[int]:
        n = len(boxes)
        result = [0] * n
       
        balls = operations = 0
        for idx, box in enumerate(boxes):
            result[idx] += operations
            if(box == '1'):
                balls += 1
            operations += balls
        balls = operations = 0
        for i in range(n - 1, -1, -1):
            result[i] += operations
            if(boxes[i] == '1'):
                balls += 1
            operations += balls
        return result