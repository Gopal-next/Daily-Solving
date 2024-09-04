class Solution:
    
    #Function to find the smallest positive number missing from the array.
    def missingNumber(self,arr,n):
        #Your code here
        arr.sort()
        count  = 1
        for i in range(n):
            if arr[i] == count:
                count +=1
        return count
