class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
            
        p_count = {}
        s_count = {}
        
        # Initialize the frequency maps for string p and the first window of s
        for i in range(len(p)):
            p_count[p[i]] = p_count.get(p[i], 0) + 1
            s_count[s[i]] = s_count.get(s[i], 0) + 1
            
        # If the first window matches, index 0 is an answer
        result = [0] if p_count == s_count else []
        
        # Slide the window across string s
        left = 0
        for right in range(len(p), len(s)):
            # Add the incoming character on the right
            s_count[s[right]] = s_count.get(s[right], 0) + 1
            
            # Remove the outgoing character on the left
            s_count[s[left]] -= 1
            if s_count[s[left]] == 0:
                del s_count[s[left]]
                
            left += 1
            
            # Check if the current window matches p's frequency map
            if s_count == p_count:
                result.append(left)
                
        return result    