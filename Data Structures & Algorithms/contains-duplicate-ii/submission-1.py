class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        counter = defaultdict(int)

        for i in range(len(nums)):
            if counter[nums[i]]:
                if abs(counter[nums[i]] - i - 1) <= k:
                    return True
           
            counter[nums[i]] = i + 1
            print(nums[i])
        
        return False