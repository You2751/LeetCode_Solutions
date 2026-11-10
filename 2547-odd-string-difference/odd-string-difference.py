class Solution:
    def oddString(self, words: list[str]) -> str:
        dic = defaultdict(list)
        for idx, word in enumerate(words):
            arr = (len(word) - 1) * [0]
            for idx2 in range(len(word) - 1):
                arr[idx2] = ord(word[idx2 + 1])- ord(word[idx2])
            dic[tuple(arr)].append(word)
        for key, lst in dic.items():
            if(len(lst) == 1):
                return lst[0]
