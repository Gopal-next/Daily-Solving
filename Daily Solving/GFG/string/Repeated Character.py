'''
https://www.geeksforgeeks.org/problems/repeated-character2058/1?page=1&category=Strings&difficulty=Basic&sortBy=difficulty
'''


class Solution:
    def firstRep(self, s):
        # code here
        dic = {}
        
        for i in s:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        for i in s:
            if dic[i] > 1:
                return i
        
        # If no repeating character is found, return '#'
        return '#'