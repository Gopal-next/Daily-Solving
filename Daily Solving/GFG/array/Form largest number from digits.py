class Solution:
    def MaxNumber(self, arr):
        #code here.
        arr.sort(reverse=True)
        return ''.join(map(str, arr))

# make it again without builtin