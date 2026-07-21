class Solution(object):
    def reverseWords(self, s):
        words = []
        i, n = 0, len(s)
        while i < n:
            if s[i] == ' ':
                i += 1
                continue
            j = i
            while j < n and s[j] != ' ':
                j += 1
            words.append(s[i:j])
            i = j
        return ' '.join(words[::-1])