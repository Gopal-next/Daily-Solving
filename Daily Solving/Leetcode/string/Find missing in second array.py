
class Solution:
    def findMissing(self,a,b,n,m):
    # code here
        # res = []
        # b = set(b)
        b = set(b)
        
        # for num in a:
        #     if num not in b:
        #         res.append(num)
        return [num for num in a if num not in b]