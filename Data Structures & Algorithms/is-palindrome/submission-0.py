class Solution:
    def isPalindrome(self, s: str) -> bool:
        a=[]
        for i in range(len(s)):
            if s[i].isalnum():
                a.append(s[i].lower())
        a="".join(a)
        if a==a[::-1]:
            return True
        else:
            return False