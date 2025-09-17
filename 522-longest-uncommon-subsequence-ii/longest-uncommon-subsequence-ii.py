class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        result = -1
        for idx1, word1 in enumerate(strs):
            subsequence_check = False
            for idx2, word2 in enumerate(strs):
                if(idx1 == idx2):
                    continue
                if(self.is_subsequence(word2, word1)):
                    subsequence_check = True
                    break
            if(not subsequence_check):
                result = max(result, len(word1))
        return result

    def is_subsequence(self, template, word):
        ptr1 = ptr2 = 0
        while(ptr1 < len(template) and ptr2 < len(word)):
            if(template[ptr1] == word[ptr2]):
                ptr2 += 1
            ptr1 += 1
        return ptr2 == len(word)