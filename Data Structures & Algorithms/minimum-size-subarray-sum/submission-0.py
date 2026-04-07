class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        total = 0
        mlength = float('inf')
        length = 0

        while len(nums) > right:

            total += nums[right]
            length += 1
            if total >= target:
                mlength = min(length, mlength)
                while total >= target:
                    mlength = min(length, mlength)
                    total -= nums[left]
                    left += 1
                    length -= 1
                

            right += 1


        return mlength if type(mlength) == int else 0