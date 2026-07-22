class Solution(object):
    def plusOne(self, digits):
        num=""
        for digit in digits:
            num+=str(digit)
        
        num=int(num)+1
        result=[]

        for digit in str(num):
            result.append(int(digit))

        return result