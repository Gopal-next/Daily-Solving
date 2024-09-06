class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr):
        ##Your code here
        max_so_far = float('-inf')
        max_ending = 0
        for i in range(len(arr)):
            max_ending = max_ending + arr[i]
            if max_so_far < max_ending:
                max_so_far = max_ending
            if max_ending < 0:
                max_ending = 0
        return max_so_far
