class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red , white  = 0,0
        for i in range(len(nums)):
            if nums[i] ==0:
                red += 1
            if nums[i] ==1:
                white += 1
        for i in range(red):
            nums[i] = 0
        for j in range(red, red+white):
            nums[j] = 1
        for j in range(red+white, len(nums)):
            nums[j] = 2
        