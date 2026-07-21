class Solution(object):
    def minWindow(self, s, t):
        need = Counter(t)
        missing = len(t)
        left = start = 0
        best = ""
        
        for right, c in enumerate(s):
            missing -= need[c] > 0
            need[c] -= 1
            while missing == 0:
                if not best or right - left + 1 < len(best):
                    best = s[left:right+1]
                need[s[left]] += 1
                missing += need[s[left]] > 0
                left += 1
        
        return best