class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        memo = {}

        def rec(index):
            if index == n:
                return True
            
            if index in memo:
                return memo[index]

            for end in range(index + 1, n + 1):
                # print(string)
                if s[index:end] in wordDict:
                    if rec(end):
                        memo[index] = True
                        return True
                
            memo[index] = False
            return False

        return rec(0)