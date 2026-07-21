class Solution(object):
    def differenceOfSums(self, n, m):
        total = n * (n + 1) // 2
        k = n // m  # count of multiples of m in [1, n]
        num2 = m * k * (k + 1) // 2  # sum of those multiples
        num1 = total - num2
        return num1 - num2