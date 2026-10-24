class Solution:
    def scoreValidator(self, events: list[str]) -> list[int]:
        dic = {"0", "1", "2", "3", "4", "6"}
        score = counter = 0
        for event in events:
            if(counter == 10):
                return [score, counter]
            if(event in dic):
                score += int(event)
            elif(event == "W"):
                counter += 1
            elif(event == 'WD' or event == "NB"):
                score += 1
        return [score, counter]
            