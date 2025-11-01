class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        n = len(word)
        if(numFriends == 1):
            return word
        split = n - numFriends + 1
        result = ""
        for i in range(n):
            result = max(result, word[i:i + split])
        return result