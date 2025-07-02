class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        check = set()
        result = float('inf')
        left = 0
        for right, num in enumerate(cards):
            while(num in check):
                if(cards[left] == num):
                    result = min(result, right - left + 1)
                check.remove(cards[left])
                left += 1
            check.add(num)
        if(result != float('inf')):
            return result
        return -1