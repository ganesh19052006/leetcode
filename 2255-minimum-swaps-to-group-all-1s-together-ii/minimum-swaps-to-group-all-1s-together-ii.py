class Solution(object):
    def minSwaps(self, nums):
         
        # Count total number of 1's
        ones = sum(nums)
        
        # If there are 0 or 1 ones, no swaps needed
        if ones <= 1:
            return 0
            
        # Duplicate array for circular traversal
        nums = nums + nums
        
        # Count zeros in first window
        zeros = 0
        
        for i in range(ones):
            if nums[i] == 0:
                zeros += 1
                
        answer = zeros
        
        # Slide the window
        for i in range(ones, len(nums)):
            
            # Remove left element
            if nums[i - ones] == 0:
                zeros -= 1
                
            # Add right element
            if nums[i] == 0:
                zeros += 1
                
            answer = min(answer, zeros)
            
        return answer