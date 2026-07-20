class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Map to store the frequency of prefix sums
        # Base case: a prefix sum of 0 has occurred once (for subarrays starting from index 0)
        prefix_sums = {0: 1}
        
        current_sum = 0
        count = 0
        
        for num in nums:
            current_sum += num
            
            # Check if there is an old prefix sum that satisfies: current_sum - old_sum = k
            target_sum = current_sum - k
            if target_sum in prefix_sums:
                count += prefix_sums[target_sum]
                
            # Record the current prefix sum in the dictionary
            prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1
            
        return count    