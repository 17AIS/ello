class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = defaultdict(int)

        map[nums[0]] = -1

        for i in range(1, len(nums)):
            if map[target - nums[i]]:
                if map[target - nums[i]] == -1:
                    return [0, i]
                else:
                    return [ map[target - nums[i]], i]
            map[nums[i]] = i
        return 