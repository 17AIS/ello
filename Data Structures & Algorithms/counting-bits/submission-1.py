class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []
        for i in range(n+1):
            string = str(bin(i))
            count = 0
            for char in string:
                if char == '1':
                    count += 1
            output.append(count)

        return output