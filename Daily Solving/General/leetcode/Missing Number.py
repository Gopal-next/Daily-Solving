class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        su = 0
        for i in range(len(nums) +1):
            su += i
        s = 0
        for i in range(len(nums)):
            s += nums[i]
        return su-s