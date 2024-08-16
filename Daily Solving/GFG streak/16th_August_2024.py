#########   Maximize The Cut Segments

# Given Below Each intution approach copied from gfg

# Intuition
'''
As you can see in the recursion tree above , that we are solving a subproblems multiple times ,
we can use dynamic programming to avoid the repetition of same recursive calls .
'''
# Approach
'''
Dry Run:

    Consider a line segment of length n = 8 units, and the possible cut lengths are x = 2, y = 3, and z = 5. We want to find the maximum number of cut segments that can be obtained using these cut lengths.

        We create a dp array of size n + 1 (in this case, 9) and initialize all elements to -1, except for dp[0], which is set to 0.
        We start with dp[1] and continue up to dp[n] in an iterative manner.
        For i = 1, we try all possible cuts (x = 2, y = 3, and z = 5), but we cannot make any cut as all cut lengths are greater than i. Hence, dp[1] remains -1.
        For i = 2, we can make a cut of length x = 2, resulting in a remaining segment of length i - x = 0. Since dp[0] is 0, we can make one cut of length x, so dp[2] = dp[0] + 1 = 0 + 1 = 1.
        For i = 3, we can make a cut of length y = 3, resulting in a remaining segment of length i - y = 0. Since dp[0] is 0, we can make one cut of length y, so dp[3] = dp[0] + 1 = 0 + 1 = 1.
        For i = 4, we can make a cut of length x = 2, resulting in a remaining segment of length i - x = 2. Since dp[2] is 1, we can make one cut of length x, so dp[4] = dp[2] + 1 = 1 + 1 = 2.
        For i = 5, we can make a cut of length z = 5, resulting in a remaining segment of length i - z = 0. Since dp[0] is 0, we can make one cut of length z, so dp[5] = dp[0] + 1 = 0 + 1 = 1.
        For i = 6, we can make a cut of length x = 2, resulting in a remaining segment of length i - x = 4. Since dp[4] is 2, we can make two cuts of length x, so dp[6] = dp[4] + 1 = 2 + 1 = 3.
        For i = 7, we can make a cut of length y = 3, resulting in a remaining segment of length i - y = 4. Since dp[4] is 2, we can make two cuts of length y, so dp[7] = dp[4] + 1 = 2 + 1 = 3.
        For i = 8, we can make a cut of length x = 2, resulting in a remaining segment of length i - x = 6. Since dp[6] is 3, we can make three cuts of length x, so dp[8] = dp[6] + 1 = 3 + 1 = 4.
'''
# Complexity
# - Time complexity:
'''
As we using a nested loop but outer loop only runs 3 times and inner loop runs n times so overall complexity is O(3*n), which is approximately O(n).
'''

# - Space complexity:
'''  O(n) for dp array . '''

# Question

###   https://www.geeksforgeeks.org/problems/cutted-segments1642/1

# Code

class Solution:
    
    #Function to find the maximum number of cuts.
    def maximizeTheCuts(self,l,p,q,r):
        #code here

        dp = [-1]*(l + 1)

        # if length of rod is 0 then
        # total cuts will be 0
        # so, initialize the dp[0] with 0
        dp[0] = 0
    
        for i in range(l+1):
    
            # if certain length is not
            # possible
            if (dp[i] == -1):
                continue
    
            # if a segment of p is possible
            if (i + p <= l):
                dp[i + p] = (max(dp[i + p],
                                 dp[i] + 1))
    
            # if a segment of q is possible
            if (i + q <= l):
                dp[i + q] = (max(dp[i + q],
                                 dp[i] + 1))
    
            # if a segment of r is possible
            if (i + r <= l):
                dp[i + r] = (max(dp[i + r],
                                 dp[i] + 1))
    
        # if no segment can be cut then return 0
        if dp[l] == -1:
            dp[l] = 0
        # return value corresponding
        # to length l
        return dp[l]