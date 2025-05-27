class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        counter = Counter(word2)
        result = left = 0
        match = len(counter)
        for right, ch in enumerate(word1):
            counter[ch] -= 1
            if(counter[ch] == 0):
                match -= 1
            while(match == 0):
                if(counter[word1[left]] == 0):
                    match += 1
                counter[word1[left]] += 1
                left += 1
            result += left
        return result
