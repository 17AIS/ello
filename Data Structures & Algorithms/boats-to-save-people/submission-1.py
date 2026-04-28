class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        total = 0
        # print(people)
        while people:
            if len(people) == 1:
                total += 1
                break
            elif limit >= people[0] + people[-1]:
                people.pop()
                people.pop(0)
                total += 1
            else:
                people.pop()
                total += 1
            
            # print(people)


        return total
            