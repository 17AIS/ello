class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        arr = []
        total = 0
        count = 0
        left = 0
        right = 0

        while right < len(fruits):
            arr.append(fruits[right])
            count += 1
            
            while len(set(arr)) > 2:
                arr.pop(0)
                left += 1
                count -= 1
            print(count, right)
            total = max(total, count)

            right += 1

        return total