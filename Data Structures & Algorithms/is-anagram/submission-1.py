class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        count = {}

        for i in range(len(s)):
            count[s[i]] = count.get(s[i], 0) + 1

        for j in range(len(t)):
            count[t[j]] = count.get(t[j], 0) - 1

        for value in count.values():
            if value != 0:
                return False

        return True
            