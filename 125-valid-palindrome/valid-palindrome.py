class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Initialize two pointers at the ends of the string
        left, right = 0, len(s) - 1
        
        while left < right:
            # Move the left pointer forward if it's not alphanumeric
            while left < right and not s[left].isalnum():
                left += 1
            # Move the right pointer backward if it's not alphanumeric
            while left < right and not s[right].isalnum():
                right -= 1
                
            # Compare the characters (lowercased)
            if s[left].lower() != s[right].lower():
                return False
            
            # Move both pointers inward
            left += 1
            right -= 1
            
        return True    