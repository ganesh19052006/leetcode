class Solution(object):
    def shuffle(self, nums, n):
        result=[]
        i=0
        j=n
        while i<n:
            result.append(nums[i])
            result.append(nums[j])
            i+=1
            j+=1
        return result
        