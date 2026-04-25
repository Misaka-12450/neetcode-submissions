class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not s and not t:
            return True
        if not s or not t:
            return False
        if len(s) != len(t):
            return False

        def s_to_d(s):
            d = {}
            for c in s:
                if d.get(c):
                    d[c] += 1
                else:
                    d[c] = 1
            return d

        s_d = s_to_d(s)
        t_d = s_to_d(t)

        for k, v in s_d.items():
            if t_d.get(k) != v:
                return False

        return True
