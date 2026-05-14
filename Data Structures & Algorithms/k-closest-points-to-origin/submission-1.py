class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        heapq.heapify(h)
        for i, j in points:
            heapq.heappush(h, ((i*i + j*j) ** 0.5, [i,j]))
        
        
        value, arr = heapq.heappop(h)
        output = [[arr[0],arr[1]]]

        for i in range(k - 1):
            new, arr = heapq.heappop(h)
            print(arr)
            output.append([arr[0],arr[1]])
        
        return output