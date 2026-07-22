class Solution(object):
    def sortedSquares(self, nums):
        n = len(nums)
        result = [0] * n
        left = 0
        right = n - 1
        p = n - 1  # Position to insert into the result array from back to front
        
        while left <= right:
            left_square = nums[left] ** 2
            right_square = nums[right] ** 2
            
            if left_square > right_square:
                result[p] = left_square
                left += 1
            else:
                result[p] = right_square
                right -= 1
                
            p -= 1  # Move the result pointer backwards
            
        return result