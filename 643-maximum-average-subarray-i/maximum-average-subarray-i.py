class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Calculate the sum of the first window
        curr_sum = max_sum = sum(nums[:k])
        
        # Slide the window across the array
        for i in range(k, len(nums)):
            curr_sum += nums[i] - nums[i - k]
            if curr_sum > max_sum:
                max_sum = curr_sum
                
        return float(max_sum) / k    