class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = []
        for idx in range(len(words)):
            for idx2 in range(len(words)):
                if(words[idx] in words[idx2] and idx != idx2):
                    result.append(words[idx])
                    break
        return result