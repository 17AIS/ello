class Solution:
    def hammingWeight(self, n: int) -> int:
        print(n)
        number = 0

        for i in range(32):
            if n & 0b1 :
                number += 1
            n >>= 1
        # print(n)

        return number
