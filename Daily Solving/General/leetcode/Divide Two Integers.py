import math
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        else:
            div = dividend/divisor
            if div > 0:
                return floor(div)
            return ceil(div)