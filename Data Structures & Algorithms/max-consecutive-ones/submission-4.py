class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = consecutiveOnes = 0
        for num in nums:
            if num == 0:
                count = 0
            else:
                count+=1
                consecutiveOnes = max(count, consecutiveOnes)
        return consecutiveOnes