class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jumps = 0
        last = len(nums)-1
        for i in range(len(nums)):
            if i >jumps:
                return False
            if nums[i]+i>jumps:
                jumps = nums[i]+i
            if jumps>= last:
                return True             #by shalini
