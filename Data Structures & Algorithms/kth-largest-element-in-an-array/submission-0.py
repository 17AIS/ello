class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        new = [ -1 * i for i in nums]
        heapq.heapify(new)
        
        temp = -1
        for i in range(k):
            temp = heapq.heappop(new)
            print(temp)
        return -temp