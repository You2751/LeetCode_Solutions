class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        dic = defaultdict(int)
        for idx, email in enumerate(emails):
            email = email.split("@")
            first_half = email[0].replace(".", "").split("+")
            email[0] = first_half[0] 
            email = "@".join(email)
            dic[email] += 1
        print(dic) 
        return len(dic)