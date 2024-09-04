class Solution:
    def reverseWords(self, s: str) -> str:
        strr = s.split(' ')
        reverse = []
        for i in strr:
            reverse.append(i[::-1])
        
        return ' '.join(reverse)
        