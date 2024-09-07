class Solution:
    def findNth(self,n):
        #code here
        
        result = 0
        p =1
        while n>0:
            result += (p*(n%9))
            
            n = n//9
            
            p = p*10
        return result