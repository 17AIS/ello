class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        left = 0
        for num in nums:
            if num != val:
                nums[left] = num
                count += 1
                left += 1
        return count