class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        result = []
        counter = Counter(friends)
        for ord in order:
            if(ord in counter):
                result.append(ord)
        return result