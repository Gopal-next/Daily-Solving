'''
https://www.geeksforgeeks.org/problems/count-digits5716/1?page=2&difficulty=Easy&sortBy=submissions
'''

class Solution:
    def evenlyDivides (self, N):
        # code here
        num = str(N)
        count = 0
        for i in range(len(num)):
            if int(num[i]) == 0:
                count = count
            elif N % int(num[i]) ==0:
                count += 1
        return count
    

#User function Template for python3


class Solution:
    def evenlyDivides (self, N):
        # code here
        count = 0  
        if N == 0:
            return 0 
        original_N = N 
        while N != 0:
            digit = N % 10
            if digit != 0 and original_N % digit == 0:
                count += 1
            N //= 10

        return count
