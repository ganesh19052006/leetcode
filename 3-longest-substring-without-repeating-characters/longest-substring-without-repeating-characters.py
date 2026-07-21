class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        left = max_len = 0
        
        for right, char in enumerate(s):
            # If char is seen inside current window, move left pointer past its last position
            if char in seen and seen[char] >= left:
                left = seen[char] + 1
                
            seen[char] = right
            max_len = max(max_len, right - left + 1)
            
        return max_len    