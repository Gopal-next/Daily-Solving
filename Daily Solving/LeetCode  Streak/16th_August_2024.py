# Maximum Distance in Arrays

# ALl given Intution, Approach of copy from https://leetcode.com/problems/maximum-distance-in-arrays/solutions/5643505/python-simple-detailed-solution/?source=submission-ac here.

# Intuition
'''
Since each array is sorted, the smallest number in any array is at the start, and the largest number is at the end. 
To maximize the distance, you should aim to subtract the smallest number from one array from the largest number in a different array.

Here's the trick: As you iterate through the arrays, you can keep track of the smallest and largest numbers encountered so far. For each new array, you can check the potential maximum distance by comparing:

    The last element of the current array with the smallest number encountered so far.
    The first element of the current array with the largest number encountered so far.

This way, you ensure that you are always comparing the extremes (largest and smallest) from different arrays to find the maximum distance.
'''
# Approach
'''
Initialize Variables: Start by initializing small and big with the first element and the last element of the first array, respectively. 
Also, initialize max_distance to keep track of the maximum distance found so far.
Iterate Through Arrays: Starting from the second array, for each array:

    Calculate the potential maximum distance by comparing the last element of the current array with small, and the first element of the current array with big.
    Update max_distance if the current comparison yields a larger distance.
    Update small and big to keep track of the smallest and largest elements encountered so far.

Return Result: After iterating through all arrays, return max_distance
'''
# Complexity

# - Time complexity:
'''
The time complexity of this solution is O(m), where m is the number of arrays. We only iterate through the arrays once, performing constant-time operations at each step.
'''
# - Space complexity:
'''
The space complexity is O(1) because we are only using a few variables (small, big, max_distance) to track the necessary information as we iterate through the arrays. No additional data structures are required.
'''

# Question
'''
https://leetcode.com/problems/maximum-distance-in-arrays/description/?source=submission-ac
'''

# Code

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        minn = arrays[0][0]
        maxx = arrays[0][-1]
        result = 0
        for i in range(1,len(arrays)):
            result = max(result, abs(arrays[i][-1] - minn), abs(maxx - arrays[i][0]))

            minn = min(minn, arrays[i][0])
            maxx = max(maxx, arrays[i][-1])
        return result
