class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        def is_vowel(char):
            return char in {'a', 'e', 'i', 'o', 'u'}
        def check(k):
            counter = defaultdict(int)
            left = result = constants = 0
            for right, char in enumerate(word):
                if(is_vowel(char)):
                    counter[char] += 1
                else:
                    constants += 1
                while(len(counter) == 5 and constants >= k):
                    result += len(word) - right
                    if(is_vowel(word[left])):
                        counter[word[left]] -= 1
                        if(counter[word[left]] == 0):
                            del counter[word[left]]
                    else:
                        constants -= 1
                    left += 1
            return result
        return check(k) - check(k + 1)
