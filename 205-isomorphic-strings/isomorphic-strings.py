class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False

        map_st = {}
        map_ts = {}

        for cs, ct in zip(s, t):
            if cs in map_st and map_st[cs] != ct:
                return False
            if ct in map_ts and map_ts[ct] != cs:
                return False
            map_st[cs] = ct
            map_ts[ct] = cs

        return True
        