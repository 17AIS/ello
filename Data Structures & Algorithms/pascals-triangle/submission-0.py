class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output = [[1]]

        for i in range(2, numRows + 1):
            ans = [1]
            # start = 0

            for j in range(1, i):
                if j == i - 1:
                    ans.append(1)
                else:
                    ans.append(output[-1][j-1] + output[-1][j])

            output.append(ans)

        return output
        # 1
        # 1 1
        # 1 2 1 
        # 1 3 3 1 
        # 1 4 6 4 1

