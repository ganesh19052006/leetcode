class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates = []
        
        for num in nums:
            # Use the absolute value to find the target index (0-indexed)
            index = abs(num) - 1
            
            # If the value at that index is already negative, it's a duplicate
            if nums[index] < 0:
                duplicates.append(abs(num))
            else:
                # Mark it as visited by negating it
                nums[index] = -nums[index]
                
        return duplicates    