class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        position = 0
        moves = {"RIGHT":1, "LEFT":-1, "UP":-n, "DOWN":n}
        for comm in commands:
            position += moves[comm]
        return position