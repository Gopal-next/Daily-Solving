'''
https://www.geeksforgeeks.org/problems/remove-and-reverse--170634/1?page=1&category=Strings&difficulty=Medium&sortBy=difficulty
'''


class Solution:
    def removeReverse(self, S): 
        #code here
        S = list(S)
        
        while True:
            freq = {}
            for i in S:
                if i not in freq:
                    freq[i] = 1
                else:
                    freq[i] += 1 
            repeat = False
            for i in range(len(S)):
                if freq[S[i]] >1:
                    S.pop(i)
                    S.reverse()
                    repeat = True
                    break
            if not repeat:
                break
        return ''.join(S)