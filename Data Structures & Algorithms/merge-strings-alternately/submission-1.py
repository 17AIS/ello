class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        one = list(word1)
        two  = list(word2)
        output = ""
        print(min(len(one), len(two)))
        for i in range((min(len(one), len(two)))):
            print(i)
            output += one.pop(0) + two.pop(0)
        
        while one:
            output += one.pop(0)

        while two:
            output += two.pop(0)
        
        return output
