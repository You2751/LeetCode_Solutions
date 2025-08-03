class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def is_subsequence(template, word):
            ptr1 = ptr2 = 0
            while(ptr1 < len(template) and ptr2 < len(word)):
                if(template[ptr1] == word[ptr2]):
                    ptr1 += 1
                    ptr2 += 1
                else:
                    ptr1 += 1
            return ptr2 == len(word)
        strs.sort(key = lambda x:-len(x))
        for left in range(len(strs)):
            word = strs[left]
            common = False
            for right in range(len(strs)):
                if(right == left):
                    continue
                if(is_subsequence(strs[right], word)):
                    common = True
                    break
            if(not common):
                return len(word)
        return -1