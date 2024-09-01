class Solution:
    def countWrongPlacedBalls(self, s):
        # return len(s)
        # code here
        c = 0
        for i in range(len(s)):
            if s[i] == 'R' and (i+1) % 2 ==0:
                c += 1
            elif s[i] == 'B' and (i+1) % 2 !=0:
                c +=1
        return c