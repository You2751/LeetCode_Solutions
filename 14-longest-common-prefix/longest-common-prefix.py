class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def match(word1, word2):
            idx1 = idx2 = 0
            while(idx1 < len(word1) and idx2 < len(word2)):
                if(word1[idx1] == word2[idx2]):
                    idx1 += 1
                    idx2 += 1
                else:
                    break
            result = word1[:idx1]
            return result
        prefix = strs[0]
        for i in range(1, len(strs)):
            prefix = match(prefix, strs[i])
        return prefix 