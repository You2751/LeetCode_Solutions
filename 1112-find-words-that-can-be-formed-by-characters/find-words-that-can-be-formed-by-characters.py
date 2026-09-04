class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        result = 0
        counter = Counter(chars)
        for word in words:
            n = len(word)
            counter_word = Counter(word)
            if(all(counter_word[c] <= counter[c] for c in counter_word.keys())):
                result += n
        return result