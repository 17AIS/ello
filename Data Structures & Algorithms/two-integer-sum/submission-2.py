class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = defaultdict(int)
        index[nums[0]] = -1
        

        for i in range(1, len(nums)):
            j = index[target-nums[i]]

            if j:
                if j == -1:
                    return [0,i]
                else: 
                    return [j, i]
            
            index[nums[i]] = i
        return [0,0]