class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        while operations:
            value = operations.pop(0)
            if value == '+':
                one = stack[-1]
                two = stack[-2]
                stack.append(one + two)
            elif value == 'C':
                stack.pop()
            elif value == 'D':
                stack.append(int(stack[-1])*2)
            else:
                stack.append(int(value))
            print(stack)
        return sum(stack)

