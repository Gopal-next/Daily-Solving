class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        nums.sort()
        maxxx = float('-inf')
        for i in range(len(nums)-1):
            new = nums[i+1] - nums[i]
            if new  > maxxx:
                maxxx= new
        return maxxx