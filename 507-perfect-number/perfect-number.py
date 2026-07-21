class Solution(object):
    def checkPerfectNumber(self, num):
        if num==1:
            return False

        total=1

        i=2
        while i*i<=num:
            if num%i==0:
                total+=i

                if i*i!=num:
                    total+=num//i
            i+=1
        return total==num