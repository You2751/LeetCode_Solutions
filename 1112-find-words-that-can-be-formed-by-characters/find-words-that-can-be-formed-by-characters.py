class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        result = 0
        counter = Counter(chars)
        for word in words:
            n = len(word)
            counter_word = Counter(word)
            if(not(counter_word - counter)):
                result += n
        return result