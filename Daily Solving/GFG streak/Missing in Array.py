class Solution:
    def missingNumber(self,array,n):
        # code here
        a = ((n)*(n+1))//2
        b = sum(array)
        c = a-b
        return c