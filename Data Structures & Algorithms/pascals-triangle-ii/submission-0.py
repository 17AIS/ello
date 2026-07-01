class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        output = [[1]]
        

        for i in range(2, rowIndex + 2):
            ans = [1]
            # start = 0

            for j in range(1, i):
                if j == i - 1:
                    ans.append(1)
                else:
                    ans.append(output[-1][j-1] + output[-1][j])

            output.append(ans)

        return output[-1]