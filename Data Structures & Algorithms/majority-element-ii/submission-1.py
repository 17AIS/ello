class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        numbers = defaultdict(int)
        output = defaultdict(int)
        n = len(nums) // 3
        for num in nums:
            numbers[num] += 1
            if numbers[num] > n:
                output[num] += 1
        

        ans = [key for key in output.keys()]
        return ans

