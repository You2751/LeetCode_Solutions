class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        def is_vowel(char):
            return char in {'a', 'e', 'i', 'o', 'u'}
        def substrings(k):
            counter = defaultdict(int)
            left = constants = result = 0
            for right, char in enumerate(word):
                if(is_vowel(char)):
                    counter[char] += 1
                else:
                    constants += 1
                while(constants >= k and len(counter) == 5):
                    left_char = word[left]
                    left += 1
                    if(is_vowel(left_char)):
                        counter[left_char] -= 1
                        if(counter[left_char] == 0):
                            del counter[left_char]
                    else:
                        constants -= 1
                result += left
            return result
        return substrings(k) - substrings(k + 1) 
