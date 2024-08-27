'''
https://www.geeksforgeeks.org/problems/max-sum-in-sub-arrays0824/1?page=6&category=Arrays&difficulty=Easy&sortBy=difficulty
'''

class Solution:
    def pairWithMaxSum(self, arr):
        # Your code goes here
    
        max_sum = 0
        for i in range(1,len(arr)):
            summ = arr[i] + arr[i-1]
            max_sum = max(max_sum, summ)
        return max_sum