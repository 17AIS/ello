class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        output = []

        def rec(index, arr):
            if index > len(nums) - 1:
                return 
            if sum(arr) == target:
                if arr not in output:
                    output.append(arr.copy())
                return 
            if sum(arr) > target:
                return
            
            rec(index+1, arr.copy())
            arr.append(nums[index])
            rec(index+1, arr.copy())
            rec(index, arr.copy())




        rec(0, [])
        return output