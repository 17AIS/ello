class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hi = defaultdict(str)
        thing = set()
        for i in range(len(s)):
            if not hi[s[i]]:
                if t[i] in thing:
                    return False
                hi[s[i]] = t[i]
                thing.add(t[i])
            else:
                if hi[s[i]] != t[i]:
                    return False
        print(hi)
        return True 