class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        judge = [True] * n
        trusting = [0] * n

        for i in range(len(trust)):
            judge[trust[i][0]-1] = False
            trusting[trust[i][1]-1] += 1
        output = -1
        flag = False
        for i in range(len(judge)):
            if judge[i] and trusting[i] == n-1:
                output = i + 1
                if flag:
                    return -1

        return output