class Solution:
    def countSubstrings(self, s: str) -> int:
        count = len(s)

        def palindrome(string):
            # print(string)
            return string == string[::-1]

        for i in range(2, len(s) + 1):
            for j in range(len(s) - i + 1):
                if palindrome(s[j:j+i]):
                    count +=1 

        return count
