class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        cards_count = Counter(deck).values()
        gcd_value = reduce(gcd, cards_count)
        return gcd_value >= 2