class Solution(object):
    def subtractProductAndSum(self, n):
        product=1
        sumofdigits=0

        while n>0:
            digit =n%10
            product*=digit
            sumofdigits+=digit
            n//=10
        
        return product-sumofdigits