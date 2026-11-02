class Solution:
    def minMoves(self, nums: List[int]) -> int:
        moves = 0
        max_num = max(nums)
        for num in nums:
            moves += max_num - num
        return moves