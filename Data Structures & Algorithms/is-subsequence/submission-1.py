class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        first = 0
        if len(s) == 0:
            return True


        for char in t:
            if char == s[first]:
                first += 1
            if first >= len(s):
                return True

        
        return False