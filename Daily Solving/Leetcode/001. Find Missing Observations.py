class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        remaining_sum = mean * (n + len(rolls)) - sum(rolls)
        if remaining_sum > 6*n or remaining_sum <n:
            return []
        res = []
        while n:
            d = min(6,remaining_sum -n +1)
            res.append(d)
            remaining_sum -= d
            n -= 1
        return res