class Solution:
	def minJumps(self, arr):
	    #code here
	    n = len(arr)
        x = y = jumps = 0
        
        for i in range(n-1):
            y = max(y, i+arr[i])
            if x ==i:
                if y ==i:
                    return -1
                jumps += 1
                x=y
        return jumps
        # 
#         n is length of the array, x is current jump, y is max jump we can take and jumps is count of minimum jumps we need to reach the end of the array

# run the for loop till we reach the last element of the array
        # count = 0