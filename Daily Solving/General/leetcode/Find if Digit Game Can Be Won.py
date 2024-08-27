class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        single = 0
        double = 0

        for i in range(len(nums)):
            if len(str(nums[i])) == 1:
                single += nums[i]
            else:
                double += nums[i]
        return True if single > double or double > single else False 