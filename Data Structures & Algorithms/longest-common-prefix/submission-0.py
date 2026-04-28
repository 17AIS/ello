class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ret = strs[0]
        if len(strs) == 1:
            return ret
        
        for i in range(1, len(strs)):
            temp = ""
            for j in range(len(strs[i])):
                if j > len(ret) - 1:
                    break
                if strs[i][j] != ret[j]:
                    break
                
                temp += strs[i][j]
            ret = temp

        return ret