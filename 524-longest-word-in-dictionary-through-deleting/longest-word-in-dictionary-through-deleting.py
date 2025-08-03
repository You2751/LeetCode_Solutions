class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        result = ""
        for word in dictionary:
            condition_one = self.is_subsequence(s, word)
            condition_two = len(word) > len(result)
            condition_three = len(word) == len(result) and word < result
            if(condition_one and (condition_two or condition_three)):
                result = word
        return result
    def is_subsequence(self, s, word):
        ptr1 = ptr2 = 0
        while(ptr1 < len(s) and ptr2 < len(word)):
            if(s[ptr1] == word[ptr2]):
                ptr1 += 1
                ptr2 += 1
            else:
                ptr1 += 1
        return ptr2 == len(word)