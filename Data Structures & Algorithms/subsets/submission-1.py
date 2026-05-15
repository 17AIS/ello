class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output =[[]]

        def rec(index, arr):
            if index > len(nums) - 1:
                return
            temp = arr.copy()
            rec(index + 1, temp)
            output.append(arr)
            # print(output)
            arr.append(nums[index])
            temp2 = arr.copy()
            rec(index + 1, temp2)


        rec(0, [])
        return output

        