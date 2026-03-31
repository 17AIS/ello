class Solution:
    def customSortString(self, order: str, s: str) -> str:
        di = defaultdict(int)

        for char in s:
            di[char] += 1

        output = ''

        for char in order:
            if di[char]:
                output += char * di[char]
                di[char] = 0

        for char in di.keys():
            output += char * di[char]
            di[char] = 0
        return output