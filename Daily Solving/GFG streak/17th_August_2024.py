class Solution:   
    def peakElement(self,arr, n):
        # Code here
        maxx = max(arr)
        for i in range(n):
            if arr[i] == maxx:
                return i