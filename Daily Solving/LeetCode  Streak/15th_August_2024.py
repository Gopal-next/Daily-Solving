####   Lemonade Change


# Intuition
'''
In this today challenge , customer going to pay to buy the lemonade like as 5 dollar , 10 dollar 0r 20 dollar.
By three ways we can achieve the solution. 
As one lemonade cost 5 dollar, he will take in lemonade of 5 dollar, others if they give 10 dollar ,  he need to give the change of 5 dollar or they need to return False.
Other scenario cutomer can give 20 dollar so it he has to give 15 dollar in this scenario he has to give 3 5 dollar or
one 10 dollar and one 5 dollar else if they dont have they need to return False

'''

# Complexity
''' - Time complexity: O(n)

The algorithm loops over the length of bills once, taking O(n) time. 
All operations within the loop are constant time operations.
'''


'''- Space complexity: O(1)

The algorithm does not use any additional data structures that scale with the input size.
Thus, the space complexity remains constant.
'''


# Code

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        if bills[0] > 5:
            return False

        five = 0
        ten =0 
        for i in bills:
            if i == 5:
                five += 1
            elif i == 10:
                if five > 0:
                    five -= 1
                    ten += 1
                else:
                    return False
            else:
                if five > 0 and ten >0:
                    five -= 1
                    ten -= 1
                elif five >=3 :
                    five -= 3
                else:
                    return False
        return True
        
