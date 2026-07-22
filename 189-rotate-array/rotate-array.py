class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k %= n  # handle k larger than array length

        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        reverse(0, n - 1)      # reverse whole array
        reverse(0, k - 1)      # reverse first k elements
        reverse(k, n - 1)      # reverse remaining elements