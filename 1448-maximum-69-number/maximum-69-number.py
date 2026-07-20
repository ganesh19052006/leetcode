class Solution(object):
    def maximum69Number (self, num):
        num=str(num)

        max_num_str=num.replace('6','9',1)

        return int(max_num_str)
        